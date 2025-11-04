class Category:
    product_count = 0
    category_count = 0

    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1  # увеличиваем число категорий
        Category.product_count += len(self.products)  # увеличиваем общее число товаров

