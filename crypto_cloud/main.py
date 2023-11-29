import logging

from _decimal import Decimal
from aiohttp import ClientSession

from crypto_cloud.types.enum import InvoiceStatus, Currency
from crypto_cloud.types.invoice import Invoice

logger = logging.getLogger(__name__)


class CryptoCloud:
    def __init__(self,
                 shop_id: str,
                 api_key: str,
                 currency: str | None):
        self.shop_id = shop_id
        self.headers: dict[str, str] = {f"Authorization": f"Token {api_key}"}
        self.currency = Currency[currency]

    def _check_errors(self, status_code: int, response_json: dict):
        if response_json['status'] == 'error' or status_code != 200:
            match status_code:
                case 406:
                    raise ConnectionRefusedError(response_json['error'])
                case 401 | 400:
                    raise ValueError(response_json['error'])
                case _:
                    raise NotImplementedError(response_json['error'])

    async def create_invoice(self,
                             amount: Decimal,
                             order_id: str = None,
                             email: str = None) -> Invoice:
        params = {
            'shop_id': self.shop_id,
            'amount': amount,
            'currency': self.currency.value,
        }
        if order_id is not None:
            params['order_id'] = order_id
        if email is not None:
            params['email'] = email
        async with ClientSession(headers=self.headers) as s:
            response = await s.post('https://api.cryptocloud.plus/v1/invoice/create', data=params)
            response_json = await response.json(encoding='utf-8')
            logger.debug(f'Crypto Cloud create invoice {response.status} {response_json}')
            self._check_errors(response.status, response_json)
        return Invoice(**response_json)

    async def check_invoice(self, invoice_id: str) -> InvoiceStatus:
        async with ClientSession(headers=self.headers) as s:
            response = await s.get(f"https://api.cryptocloud.plus/v1/invoice/info?uuid=INV-{invoice_id}")
            response_json = await response.json(encoding='utf-8')
            logger.debug(f'Crypto Cloud check invoice {response.status} {response_json}')
            self._check_errors(response.status, response_json)
            return InvoiceStatus(response_json['status_invoice'])
