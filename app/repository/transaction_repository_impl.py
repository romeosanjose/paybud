import json

from app.repository.abstract_repository import AbstractRepository
from app.repository.transaction_repository import TransactionRepository

class TransactionRepositoryImpl(AbstractRepository, TransactionRepository):
    def __init__(self):
        self.session = {}

    def find_by_user_id(self, user_id):
        if user_id in self.session:
            return json.loads(self.session[user_id])
        else:
            return None

    def store_by_user_id(self, transaction):
        transaction_list = []
        if transaction.get_user_id() in self.session:
            record = json.loads(self.session[transaction.get_user_id()])
            for t in record:
                transaction_list.append(t)
            transaction_list.append(transaction.to_array())
        else:
            transaction_list.append(transaction.to_array())

        self.session[transaction.get_user_id()] = json.dumps(transaction_list)