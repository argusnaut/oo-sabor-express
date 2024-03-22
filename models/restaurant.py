class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    @classmethod
    def list_restaurants(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}")

    @property
    def active(self):
        return "☑" if self._active else "☐"

    def change_status(self):
        self._active = not self._active


restaurant_praca = Restaurant("praça", "Gourmet")
restaurant_praca.change_status()
restaurant_pizza = Restaurant("pizza Express", "Italiana")

Restaurant.list_restaurants()
