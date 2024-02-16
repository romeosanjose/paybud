import unittest
from app.entity.transaction import Transaction
from app.repository.transaction_repository_impl import TransactionRepositoryImpl
from app.use_case.cash_in import CashIn
from app.entity.currency import EURCurrency, Currency

class CashInTest(unittest.TestCase):
    def cash_in_data_provider(self):
        return [
            ('2016-01-10', 2, 'legal', 1000000.00, 'EUR', 5.00),
            ('2016-01-05', 1, 'natural', 200.00, 'EUR', 0.06)
        ]

    def test_do_cash_in(self):
        for date, user_id, user_type, amount, currency, expected_comission in self.cash_in_data_provider():
            if currency == 'EUR':
                currency_obj = EURCurrency()

            transaction = Transaction()
            transaction.set_amount(amount)
            transaction.set_transaction_date(date)
            transaction.set_user_id(user_id)
            transaction.set_user_type(user_type)

            cash_in = CashIn(TransactionRepositoryImpl())
            transaction = cash_in.do_cash_in(transaction, currency_obj)
            self.assertEqual(expected_comission, transaction.get_converted_comission())

if __name__ == '__main__':
    unittest.main()