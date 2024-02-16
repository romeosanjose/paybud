import math
from date_checker import DateChecker

class CashOutOperation:
    def previous_transaction(self, extracted_transactions):
        return extracted_transactions[-1] if extracted_transactions else False

    def is_already_acquired_discount(self, extracted_transactions):
        for et in extracted_transactions:
            if et['is_discounted'] == True:
                return True
        return False

    def fill_transaction(self, transaction, currency, comission, converted_comission, converted_amount, is_discounted=False, is_previous_free=False):
        transaction.set_comission(comission)
        transaction.set_currency(currency.get_currency_code())
        transaction.set_converted_comission(converted_comission)
        transaction.set_converted_amount(converted_amount)
        transaction.set_is_discounted(is_discounted)
        transaction.set_is_previous_free(is_previous_free)
        transaction.set_transaction_id(transaction.generate_salt(
            [f"{transaction.get_user_id()}-{transaction.get_transaction_date()}"]
        ))

        return transaction

    def calculate_comission(self, amount):
        return (amount * 0.3) / 100

    def calculate_total_amount_transaction(self, extracted_transactions):
        return sum(et['converted_amount'] for et in extracted_transactions)

    def extract_transactions_within_the_week(self, date, persisted_transactions):
        transactions = []
        days_of_week = DateChecker().get_dates_in_week_of_date(date)
        if persisted_transactions:
            for transaction in persisted_transactions:
                if transaction['transaction_date'] in days_of_week:
                    transactions.append(transaction)
        return transactions

    def convert_to_eur(self, amount, currency):
        return amount / currency.get_currency_value()

    def convert_to_current_currency(self, amount, currency):
        return round(self.round_up(amount * currency.get_currency_value(), 2), 2)

    def round_up(self, value, places=0):
        if places < 0:
            places = 0
        mult = pow(10, places)
        return math.ceil(value * mult) / mult