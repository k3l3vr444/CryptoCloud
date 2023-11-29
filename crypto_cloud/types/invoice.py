from pydantic import BaseModel, StrictStr, HttpUrl

from crypto_cloud.types.enum import Status, CryptoCurrency


class Invoice(BaseModel):
    status: Status
    pay_url: HttpUrl
    invoice_id: StrictStr
    currency: CryptoCurrency
