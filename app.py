from models.restaurant import Restaurant
from models.menu.beverage import Beverage
from models.menu.dish import Dish

restaurant_praca = Restaurant("Praça", "Gourmet")
beverage_suco = Beverage("Suco de Melancia", 5.00, "Grande")
beverage_suco.apply_discount()
dish_paozinho = Dish("Pãozinho", 2.00, "O melhor pão da cidade")
dish_paozinho.apply_discount()

restaurant_praca.add_to_menu(beverage_suco)
restaurant_praca.add_to_menu(dish_paozinho)


def main():
    restaurant_praca.display_menu


if __name__ == "__main__":
    main()
