from objects.cashier import Cashier
from objects.stock_control import StockControl


class Morrisons(Cashier, StockControl):
    def order_stock(self):
        pass

    def stock_shelves(self, amount):
        pass

    def give_change(self):
        pass

    def take_money(self, amount):
        pass

