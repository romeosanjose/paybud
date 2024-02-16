from abc import ABC, abstractmethod

from app.repository.repository import Repository

class TransactionRepository(Repository):
    @abstractmethod
    def find_by_user_id(self, user_id):
        pass

    @abstractmethod
    def store_by_user_id(self, transaction):
        pass