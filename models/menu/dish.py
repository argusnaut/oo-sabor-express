from models.menu.menu_item import MenuItem


class Dish(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description

    def apply_discount(self):
        self._price -= (self._price * 0.05)
