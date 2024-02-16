from abc import ABC, abstractmethod
from math import ceil, pow

from app.entity.entity import Entity


class Currency(Entity, ABC):
    @abstractmethod
    def get_currency_value(self):
        pass

    @abstractmethod
    def get_currency_code(self):
        pass

    def convert_to_EUR(self, amount):
        return amount / self.get_currency_value()

    def convert_to_current_currency(self, amount):
        return "{:.2f}".format(self.round_up(amount * self.get_currency_value(), 2))

    def round_up(self, value, places=0):
        if places < 0:
            places = 0
        mult = pow(10, places)
        return ceil(value * mult) / mult

    @abstractmethod
    def to_array(self):
        pass