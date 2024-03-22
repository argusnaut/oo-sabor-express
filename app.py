from models.restaurant import Restaurant
from models.menu.beverage import Beverage
from models.menu.dish import Dish

restaurant_praca = Restaurant("Praça", "Gourmet")
beverage_suco = Beverage("Suco de Melancia", 5.00, "Grande")
dish_paozinho = Dish("Pãozinho", 2.00, "O melhor pão da cidade")


def main():
    print(beverage_suco)
    print(dish_paozinho)


if __name__ == "__main__":
    main()
