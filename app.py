from models.restaurant import Restaurant

restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_mexicano = Restaurant("Mexican Food", "Mexicana")
restaurant_japones = Restaurant("Japa", "Japonesa")

restaurant_mexicano.change_status()


def main():
    Restaurant.list_restaurants()


if __name__ == "__main__":
    main()
