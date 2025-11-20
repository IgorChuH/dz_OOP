import pytest
from src.product import Product
from src.category import Category

@pytest.fixture(autouse=True)
def reset_category_count():
    # Сброс значений перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0

def test_new_product():
    new_data = {
        "name": "Телефон",
        "description": "Смартфон с хорошей камерой",
        "price": 20000,
        "quantity": 10
    }

    product = Product.new_product(new_data)
    assert product.name == "Телефон"
    assert product.description == "Смартфон с хорошей камерой"
    assert product.price == 20000
    assert product.quantity == 10

@pytest.fixture
def sample_products():
    # Создадим несколько товаров для теста
    p1 = Product.new_product({
        "name": "Телефон",
        "description": "Смартфон",
        "price": 10000,
        "quantity": 5
    })
    p2 = Product.new_product({
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 50000,
        "quantity": 3
    })
    return [p1, p2]

def test_category_count():
    # Проверяем количество категорий при создании первой категории
    category1 = Category("Электроника", "Устройства и аксессуары", [
        Product.new_product({
            "name": "Телефон",
            "price": 20000,
            "quantity": 10
        })
    ])
    assert Category.category_count == 1

def test_product_count_with_instantiate():
    # Проверяем количество продуктов при создании категории с несколькими продуктами
    category2 = Category("Бытовая техника", "Аппараты для дома", [
        Product.new_product({
            "name": "Холодильник",
            "price": 30000,
            "quantity": 5
        }),
        Product.new_product({
            "name": "Стиральная машина",
            "price": 25000,
            "quantity": 3
        })
    ])
    assert Category.product_count == 2

def test_add_product():
    category3 = Category("Книги", "Все о книгах", [])
    assert Category.product_count == 0  # Должно быть 0 продуктов
    product = Product.new_product({
        "name": "Книга",
        "description": "Новая книга",
        "price": 500,
        "quantity": 10
    })
    category3.add_product(product)
    assert Category.product_count == 1  # Должно быть 1 продукт