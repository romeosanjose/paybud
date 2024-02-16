from abc import ABC, abstractmethod

class Entity(ABC):
    def generate_salt(self, words=[]):
        salt = ''
        for w in words:
            salt = salt + w
        return salt

    @abstractmethod
    def to_array(self):
        pass