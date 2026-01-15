from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта."""

    @abstractmethod
    def __init__(self):
        pass


class ProductMixin:
    """Миксин для логирования при создании объекта."""

    def __init__(self, *args, **kwargs):
        """Выводит информацию об объекте при инициализации."""
        super().__init__(
            *args, **kwargs
        )  # Сначала вызываем __init__ следующего класса в MRO
        print(self.__class__.__name__, "создан")  # Выводим информацию о создании класса

    def __repr__(self):
        return f"{self.__class__.__name__}"


class Product(ProductMixin, BaseProduct):
    """Класс продукта, наследуется от миксина ProductMixin и BaseProduct."""

    def __init__(self, name, description, price, quantity):
        """Инициализация объекта Product."""
        # Инициализация атрибутов экземпляра Product
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()  # Вызываем __init__ миксина после инициализации атрибутов

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


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self._Product__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(
            f"Нельзя добавлять продукт к смартфону: {type(self).__name__} и {type(other).__name__}"
        )


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(
            f"Нельзя добавлять продукт к смартфону: {type(self).__name__} и {type(other).__name__}"
        )
