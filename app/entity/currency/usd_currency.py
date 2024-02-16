from app.entity.currency.currency import Currency


class USDCurrency(Currency):
    def __init__(self):
        self.currency_amount = 1.1497

    def get_currency_code(self):
        return 'USD'

    def get_currency_value(self):
        return self.currency_amount