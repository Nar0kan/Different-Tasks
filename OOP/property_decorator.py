class House:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.__price = new_price
        else:
            print("Not available!")

    @price.deleter
    def price(self):
        del self.__price

example_1 = House(20000)
example_1.price = 100000
print(example_1.price)
