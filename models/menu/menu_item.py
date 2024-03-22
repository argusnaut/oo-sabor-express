class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return self._name
