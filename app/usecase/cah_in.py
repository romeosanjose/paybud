from app.usecase.cash_flow import CashFlow


class CashIn(CashFlow):
    def __init__(self, transaction_repository):
        self.transaction_repo = transaction_repository

    def do_cash_in(self, transaction, currency):
        converted_amount = self.convert_to_eur(transaction.get_amount(), currency)
        comission = self.calculate_comission(converted_amount)
        converted_comission = self.convert_to_current_currency(comission, currency)
        transaction = self.fill_transaction(transaction, currency, comission, converted_comission, converted_amount)

        return transaction

    def fill_transaction(self, transaction, currency, comission, converted_comission, converted_amount):
        transaction.set_comission(comission)
        transaction.set_currency(currency.get_currency_code())
        transaction.set_converted_comission(converted_comission)
        transaction.set_converted_amount(converted_amount)
        transaction.set_transaction_id(transaction.generate_salt(
            [f"{transaction.get_user_id()}-{transaction.get_transaction_date()}"]
        ))

        return transaction

    def calculate_comission(self, amount):
        comission = ((amount * 0.03) / 100)

        return 5.00 if comission > 5.00 else comission