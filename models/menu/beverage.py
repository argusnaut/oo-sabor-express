from models.menu.menu_item import MenuItem


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size
