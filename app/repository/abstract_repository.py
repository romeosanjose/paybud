from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def store(self, entity):
        pass