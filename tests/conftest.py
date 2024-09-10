import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_with_two_products():
    """Для тестов категории с двумя продуктами"""
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category_with_one_product():
    """Для тестов категории с одним продуктом"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def category_without_products():
    """Для тестов категории без продуктов"""
    return Category(
        name="Ноутбуки", description="Переносные компьютеры, отличаются небольшими размерами и весом", products=[]
    )


@pytest.fixture
def product():
    """Для тестов инициализации объектов класса Product"""
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def path_products_json():
    """Путь до products.json"""
    return "../OOP/data/products.json"


@pytest.fixture
def data_products_json():
    """Данные из products.json"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2],
)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product3],
)

@pytest.fixture
def products():
    """Фикстура, использующаяся для тестирования классов Product и Category"""
    return product1, product2, product3


@pytest.fixture
def categories():
    """Фикстура, использующаяся для тестирования класса Category"""
    return category1, category2


@pytest.fixture
def product_dict():
    return (
        {"name": "Phone", "description": "Some description", "price": 10000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 20000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 5000, "quantity": 1},
    )
