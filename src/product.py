class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data):
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        quantity = data.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    def quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.price * other.quantity)
