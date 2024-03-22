class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name} | {self.category}"

    def list_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f"{restaurant.name} | {restaurant.category} | {restaurant.active}")


restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_pizza = Restaurant("Pizza Express", "Italiana")

Restaurant.list_restaurants()
