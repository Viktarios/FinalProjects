class Toys:
    def __init__(self, price=0, weight=0):
        self.__price = price
        self.__weight = weight

    @property
    def price(self):
        return self.__price

    @property
    def weight(self):
        return self.__weight

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight > 0:
            self.__weight = weight
