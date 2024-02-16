from app.entity.currency.currency import Currency


class JPYCurrency(Currency):
    def __init__(self):
        self.currency_amount = 129.53

    def get_currency_code(self):
        return 'JPY'

    def get_currency_value(self):
        return self.currency_amount