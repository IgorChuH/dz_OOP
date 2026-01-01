from src.product import Product

class Category:
    name: str
    description: str
    quantity: int
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self._name = name
        self._description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, other):
        if isinstance(other, Product):
            self.__products.append(other)
            Category.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self._name}, количество продуктов: {count} шт."

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
