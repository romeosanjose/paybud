from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def store(self, entity):
        pass