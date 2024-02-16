from app.usecase.cash_out import CashOut
from app.usecase.cash_out_operation import CashOutOperation


class NATURALUserCashOut(CashOutOperation):
    def execute_cash_out(self, transaction_repository, transaction, currency, converted_amount):
        persisted_transactions = transaction_repository.find_by_user_id(transaction.get_user_id())
        extracted_transactions = self.extract_transactions_within_the_week(transaction.get_transaction_date(), persisted_transactions)
        if 0 < len(extracted_transactions) <= 2:
            transaction = self.process_comission(extracted_transactions, converted_amount, currency, transaction, is_total=True)
        else:
            transaction = self.process_comission(extracted_transactions, converted_amount, currency, transaction)

        return transaction

    def process_comission(self, extracted_transactions, converted_amount, currency, transaction, is_total=False):
        if self.is_already_acquired_discount(extracted_transactions):
            transaction = self.compute_comission(converted_amount, converted_amount, transaction, currency)
        else:
            transaction = self.compute_comission_with_rules(converted_amount, currency, transaction, extracted_transactions, is_total)

        return transaction

    def compute_comission_with_rules(self, converted_amount, currency, transaction, extracted_transactions, is_total=False):
        if converted_amount > CashOut.MAX_AMOUNT:
            excess = converted_amount - CashOut.MAX_AMOUNT
            return self.compute_comission(excess, converted_amount, transaction, currency, True)
        elif converted_amount == CashOut.MAX_AMOUNT:
            previous_txn = self.previous_transaction(extracted_transactions)
            if previous_txn and previous_txn['converted_amount'] < CashOut.MAX_AMOUNT and is_total:
                total_amount = self.calculate_total_amount_transaction(extracted_transactions) + converted_amount
                if total_amount > CashOut.MAX_AMOUNT:
                    excess = total_amount - CashOut.MAX_AMOUNT
                    transaction = self.compute_comission(excess, converted_amount, transaction, currency, False, True)
                else:
                    transaction = self.compute_comission(total_amount, converted_amount, transaction, currency, False, True)
            else:
                comission = CashOut.FREE_AMOUNT
                converted_comission = self.convert_to_current_currency(comission, currency)
                transaction = self.fill_transaction(transaction, currency, comission, converted_comission, converted_amount, True)
        else:
            transaction = self.compute_comission(converted_amount, converted_amount, transaction, currency)

        return transaction

    def compute_comission(self, amount_for_comission_compute, converted_amount, transaction, currency, is_discounted=False, is_previous_free=False):
        comission = self.calculate_comission(amount_for_comission_compute)
        converted_comission = self.convert_to_current_currency(comission, currency)

        return self.fill_transaction(transaction, currency, comission, converted_comission, converted_amount, is_discounted, is_previous_free)