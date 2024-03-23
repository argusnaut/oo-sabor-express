from models.menu.menu_item import MenuItem


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def apply_discount(self):
        self._price -= (self._price * 0.08)
