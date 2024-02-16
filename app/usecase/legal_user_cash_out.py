from app.usecase.cash_out_operation import CashOutOperation


class LegalUserCashOut(CashOutOperation):
    def execute_cash_out(self, transaction_repository, transaction, currency, converted_amount):
        return self.compute_comission(converted_amount, converted_amount, transaction, currency)

    def compute_comission(self, amount_for_comission_compute, converted_amount, transaction, currency, is_discounted=False, is_previous_free=False):
        comission = self.calculate_comission(amount_for_comission_compute)
        if comission < 0.50:
            comission = 0.00

        converted_comission = self.convert_to_current_currency(comission, currency)
        return self.fill_transaction(transaction, currency, comission, converted_comission, converted_amount, is_discounted, is_previous_free)