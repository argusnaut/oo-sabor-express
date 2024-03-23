from models.menu.menu_item import MenuItem
from models.rating import Rating


class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    @classmethod
    def list_restaurants(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")
        print(f"{("-" * 24).ljust(25)} | {("-" * 24).ljust(25)} | {("-" * 24).ljust(25)} | {("-" * 6)}")
        for restaurant in cls.restaurants:
            print(
                f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | {restaurant.active}")

    @property
    def active(self):
        return "☑" if self._active else "☐"

    def change_status(self):
        self._active = not self._active

    def add_rating(self, client, rate):
        if 0 < rate <= 5:
            rating = Rating(client, rate)
            self._rating.append(rating)

    @property
    def average_rating(self):
        if not self._rating:
            return '-'
        rating_sum = sum(rating._rating for rating in self._rating)
        rating_amount = len(self._rating)
        average = round(rating_sum / rating_amount, 1)
        return average

    def add_to_menu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def display_menu(self):
        print(f"Cardápio do restaurante {self._name}\n")
        for index, item in enumerate(self._menu, start=1):
            if hasattr(item, "_description"):
                dish_message = f"{index}. Nome: {item._name} | Preço: R${item._price} | Descrição: {item._description}"
                print(dish_message)
            else:
                beverage_message = f"{index}. Nome: {item._name} | Preço: R${item._price} | Tamanho: {item._size}"
                print(beverage_message)
