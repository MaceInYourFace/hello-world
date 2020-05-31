from abc import ABC, abstractmethod

class Cashier(ABC):

    @abstractmethod
    def take_money(self, amount):
        pass

    @abstractmethod
    def give_change(self):
        pass