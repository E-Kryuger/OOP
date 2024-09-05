class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавление объекта в приватный атрибут __products"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращение информации по товару в виде строки:
        Название продукта, _ руб. Остаток: _ шт."""
        products_str = ""
        for product in self.__products:
            products_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
