from models.restaurant import Restaurant

restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_praca.add_rating("Gui", 5)
restaurant_praca.add_rating("Lais", 4)
restaurant_praca.add_rating("Emy", 2.5)


def main():
    Restaurant.list_restaurants()


if __name__ == "__main__":
    main()
