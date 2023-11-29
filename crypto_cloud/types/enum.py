import enum


class Status(enum.Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class InvoiceStatus(enum.Enum):
    CREATED = 'created'
    PAID = 'paid'
    PARTIAL = 'partial'
    CANCELED = 'canceled'


class Currency(enum.Enum):
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'
    GBP = 'GBP'


class CryptoCurrency(enum.Enum):
    BTC = 'BTC'
    LTC = 'LTC'
    ETH = 'ETH'
    USDT = 'USDT_TRC20'
