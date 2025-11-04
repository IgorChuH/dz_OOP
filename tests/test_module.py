import pytest

from src.product import Product
from src.category import Category


@pytest.fixture()
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


def test_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


@pytest.fixture
def category():
    return Category(
        "Electronics", "Various electronic items", ["TV", "Radio", "Laptop"]
    )


def test_category_init(category):
    assert category.name == "Electronics"
    assert category.description == "Various electronic items"
    assert category.products == ["TV", "Radio", "Laptop"]


def test_class_counters():
    Category.category_count = 0
    Category.product_count = 0  # обязательно сбросить
    category = Category(
        "Electronics", "Various electronic items", ["TV", "Radio", "Laptop"]
    )
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_multiple_categories():
    # Проверка счетчиков при создании нескольких объектов
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    c1 = Category("Books", "Various books", ["Book1", "Book2"])
    c2 = Category("Clothes", "Different clothes", ["Shirt"])

    assert Category.category_count == initial_category_count + 2
    assert Category.product_count == initial_product_count + 3
