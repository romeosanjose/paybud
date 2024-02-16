import unittest
from unittest.mock import Mock
from app.entity.transaction import Transaction
from app.repository.transaction_repository_impl import TransactionRepositoryImpl
from app.use_case.cash_out import CashOut
from app.entity.currency import EURCurrency, Currency

class CashOutTest(unittest.TestCase):
    def cash_out_data_provider():
        return [
            ['2016-01-06', 1, 'natural', 30000, 'JPY', 90.00, []],
            ['2016-01-07', 1, 'natural', 1000.00, 'EUR', 0.70,
                [
                    {
                        'transaction_date': '2016-01-06',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 30000,
                        'is_discounted': False,
                        'converted_amount': 231.6065776268,
                    }
                ]
            ],
            ['2016-01-07', 1, 'natural', 100.00, 'USD', 0.30,
                [
                    {
                        'transaction_date': '2016-01-06',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 30000,
                        'is_discounted': False,
                        'converted_amount': 231.6065776268,
                    },
                    {
                        'transaction_date': '2016-01-07',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 1000.00,
                        'is_discounted': False,
                        'converted_amount': 1000.00,
                    }
                ]
            ],
            ['2016-01-10', 1, 'natural', 100.00, 'EUR', 0.30,
                [
                    {
                        'transaction_date': '2016-01-06',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 30000,
                        'is_discounted': False,
                        'converted_amount': 231.6065776268,
                    },
                    {
                        'transaction_date': '2016-01-07',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 1000.00,
                        'is_discounted': False,
                        'converted_amount': 1000.00,
                    },
                    {
                        'transaction_date': '2016-01-07',
                        'user_id': 1,
                        'user_type': 'natural',
                        'amount': 100.00,
                        'is_discounted': False,
                        'converted_amount': 100.00,
                    }
                ]
            ]
        ]

    def get_transaction_repo_mock(self, persisted_data):
        mock_object = Mock(spec=TransactionRepositoryImpl)
        mock_object.find_by_user_id.return_value = persisted_data
        return mock_object

    def test_cash_out_with_free_previous(self):
        for date, user_id, user_type, amount, currency, expected_comission, persisted_data in self.cash_out_data_provider():
            if currency == 'EUR':
                currency_obj = EURCurrency()

            transaction = Transaction()
            transaction.set_amount(amount)
            transaction.set_transaction_date(date)
            transaction.set_user_id(user_id)
            transaction.set_user_type(user_type)

            cash_out = CashOut(self.get_transaction_repo_mock(persisted_data))
            transaction = cash_out.do_cash_out(transaction, currency_obj)
            self.assertEqual(expected_comission, transaction.get_converted_comission())

    # Define other test methods here

if __name__ == '__main__':
    unittest.main()