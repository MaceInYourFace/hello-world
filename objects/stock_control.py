from abc import ABC, abstractmethod

class StockControl(ABC):

    @abstractmethod
    def stock_shelves(self, amount):
        pass

    @abstractmethod
    def order_stock(self):
        pass