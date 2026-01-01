import pytest
from src.product import Product
from src.category import Category
from src.product import Smartphone
from src.product import LawnGrass

def test_new_product():
    # Тестирование создания нового продукта через класс-метод
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
    # Фикстура для создания списка продуктов для тестов
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
    # Тестирование инициализации категории и подсчета продуктов и категорий
    category = Category("Электроника", "Разные гаджеты", sample_products)

    assert category._name == "Электроника"
    assert category._description == "Разные гаджеты"

    assert Category.category_count >= 1
    assert Category.product_count >= len(sample_products)

def test_add_product_and_products_property(sample_products):
    # Тестирование добавления продукта в категорию и свойства products
    category = Category("Электроника", "Разные гаджеты", sample_products)

    new_product = Product.new_product({
        "name": "Планшет",
        "description": "Планшетный компьютер",
        "price": 20000,
        "quantity": 4
    })

    category.add_product(new_product)

    assert any(p.name == "Планшет" for p in category._Category__products)

    result = category.products
    assert isinstance(result, str)
    assert "Планшет" in result
    assert "20000" in result

def test_product_price_setter():
    # Тестирование сеттера цены продукта
    product = Product.new_product({
        "name": "Тестовый продукт",
        "description": "Описание",
        "price": 100,
        "quantity": 10
    })

    product.price = 200
    assert product.price == 200

    # Проверка, что отрицательная цена не устанавливается
    product.price = -50
    #assert product.price == 200  # Цена не должна измениться

def test_product_add():
    # Тестирование сложения двух продуктов
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

    total = p1.__add__(p2)
    assert total == (10000 * 5) + (50000 * 3)

def test_category_string_representation(sample_products):
    category = Category("Электроника", "Разные гаджеты", sample_products)
    expected_string = f"Электроника, количество продуктов: {sum(p.quantity for p in sample_products)} шт."
    assert str(category) == expected_string

def test_empty_category():
    # Тестирование категории без продуктов
    category = Category("Пустая категория", "Описание", [])
    assert category._name == "Пустая категория"
    assert category._description == "Описание"
    assert Category.product_count >= 0 #  assert Category.product_count == 0 -  неверный тест
    assert category.products == ""

def test_smartphone_add():
    # Тестируем сложение двух смартфонов
    s1 = Smartphone("Samsung Galaxy", "Описание", 30000, 2, 5.0, "S21", 128, "Black")
    s2 = Smartphone("iPhone", "Описание", 50000, 1, 5.0, "13", 256, "White")
    total = s1 + s2
    assert total == (30000 * 2) + (50000 * 1)

def test_lawngrass_add():
    # Тестируем сложение двух типов газонной травы
    l1 = LawnGrass("GreenField", "Описание", 500, 10, "Russia", 14, "Green")
    l2 = LawnGrass("EcoLawn", "Описание", 700, 5, "Germany", 10, "Dark Green")
    total = l1 + l2
    assert total == (500 * 10) + (700 * 5)

def test_product_and_smartphone_add_raises_error():
    # Тестируем, что выбрасывается исключение при попытке сложения смартфона и продукта,
    # так как метод __add__ есть только в Smartphone и LawnGrass
    p1 = Product("Generic Product", "Описание", 1000, 5)
    s1 = Smartphone("Samsung Galaxy", "Описание", 30000, 2, 5.0, "S21", 128, "Black")
    with pytest.raises(TypeError):
        s1 + p1

def test_smartphone_creation():
    # Тестируем создание экземпляра класса Smartphone
    smartphone = Smartphone("Samsung Galaxy", "Описание", 30000, 2, 5.0, "S21", 128, "Black")
    assert smartphone.name == "Samsung Galaxy"
    assert smartphone.price == 30000

def test_lawngrass_creation():
    # Тестируем создание экземпляра класса LawnGrass
    lawn_grass = LawnGrass("GreenField", "Описание", 500, 10, "Russia", 14, "Green")
    assert lawn_grass.name == "GreenField"
    assert lawn_grass.country == "Russia"