from app.usecase.cash_flow import CashFlow


class CashOut(CashFlow):
    MAX_AMOUNT = 1000.00
    FREE_AMOUNT = 0.00

    def __init__(self, transaction_repository):
        self.transaction_repo = transaction_repository

    def do_cash_out(self, transaction, currency):
        converted_amount = self.convert_to_eur(transaction.get_amount(), currency)

        cash_out_operation_class = globals()[f"{transaction.get_user_type().capitalize()}UserCashOut"]
        cash_out_operation_object = cash_out_operation_class()

        transaction = cash_out_operation_object.execute_cash_out(self.transaction_repo, transaction, currency, converted_amount)

        self.transaction_repo.store_by_user_id(transaction)

        return transaction