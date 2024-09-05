from src.category import Category


def test_category_init(category_without_products):
    """Тест инициализации объектов класса Category"""
    assert category_without_products.name == "Ноутбуки"
    assert category_without_products.description == "Переносные компьютеры, отличаются небольшими размерами и весом"
    assert len(category_without_products.products) == 0


def test_product_count(category_with_two_products):
    assert category_with_two_products.product_count == 5


def test_category_count(category_with_one_product):
    assert category_with_one_product.category_count == 5


def test_add_product(categories, products):
    """Тестирует метод add_product"""
    categories[0].add_product(products[2])
    assert Category.product_count == 7


def test_products(categories):
    """Тест products-геттера"""
    products_str = '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    assert categories[0].products == products_str
