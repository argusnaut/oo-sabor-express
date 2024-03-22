from models.restaurant import Restaurant

restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_praca.add_rating("Gui", 10)
restaurant_praca.add_rating("Lais", 8)
restaurant_praca.add_rating("Emy", 5)


def main():
    Restaurant.list_restaurants()


if __name__ == "__main__":
    main()
