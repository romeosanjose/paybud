from app.entity.currency.currency import Currency


class EURCurrency(Currency):
    def __init__(self):
        self.currency_amount = 1

    def get_currency_code(self):
        return 'EUR'

    def get_currency_value(self):
        return self.currency_amount