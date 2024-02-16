import unittest
from app.entity.transaction import Transaction
from app.repository.transaction_repository_impl import TransactionRepositoryImpl

class PersistDataTest(unittest.TestCase):
    def test_store_data(self):
        t1a = Transaction()
        t1a.set_user_id(0000)
        t1b = Transaction()
        t1b.set_user_id(0000)

        t2a = Transaction()
        t2a.set_user_id(1111)
        t2b = Transaction()
        t2b.set_user_id(1111)

        tr1_repo = TransactionRepositoryImpl()
        tr1_repo.store_by_user_id(t1a)
        tr1_repo.store_by_user_id(t1b)

        result = tr1_repo.find_by_user_id(0000)

        self.assertEqual(2, len(result))

if __name__ == '__main__':
    unittest.main()