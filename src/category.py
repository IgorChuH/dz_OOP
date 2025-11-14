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

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return f"{self._name}, {Product.price} руб. {Category.product_count} шт."
