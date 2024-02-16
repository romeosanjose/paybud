import math

class CashFlow:
    def persist_transaction(self, transaction, transaction_repository):
        result = transaction_repository.store(transaction)
        if not result:
            raise Exception("Unable to save transaction")

    def convert_to_eur(self, amount, currency):
        return amount / currency.get_currency_value()

    def convert_to_current_currency(self, amount, currency):
        return round(self.round_up(amount * currency.get_currency_value(), 2), 2)

    def round_up(self, value, places=0):
        if places < 0:
            places = 0
        mult = pow(10, places)
        return math.ceil(value * mult) / mult