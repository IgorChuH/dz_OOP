import pytest

from src.product import Product
from src.category import Category

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

def test_category_init_and_counts(sample_products):
    category = Category("Электроника", "Разные гаджеты", sample_products)

    assert category._name == "Электроника"
    assert category._description == "Разные гаджеты"

    assert Category.category_count >= 1
    assert Category.product_count >= len(sample_products)

def test_add_product_and_products_property(sample_products):
    category = Category("Электроника", "Разные гаджеты", sample_products)

    # Создаем новый продукт
    new_product = Product.new_product({
        "name": "Планшет",
        "description": "Планшетный компьютер",
        "price": 20000,
        "quantity": 4
    })

    # Добавляем продукт
    category.add_product(new_product)

    # Проверка, что продукт добавлен во внутренний список
    assert any(p.name == "Планшет" for p in category._Category__products)

    result = category.products
    assert isinstance(result, str)
    assert "Планшет" in result
    assert "20000" in result