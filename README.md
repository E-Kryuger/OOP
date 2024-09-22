# ООП

## Описание:
В проекте реализовано несколько модулей:

---
### base_product
Модуль, содержащий абстрактный базовый класс для представления продукта\
Создан абстрактный класс <u>**BaseProduct**</u>\
В нём реализован метод `new_product`, который используется для создания нового продукта или обновления существующего.

---
### print_mixin
Модуль, содержащий класс-миксин, который при создании объекта печатает в консоль информацию.\
Создан класс <u>**PrintMixin**</u>.\
Реализован метод `__init__`, который печатает в консоль информацию, вызывая метод `__repr__`\
Метод `__repr__` возвращает в виде строки:
- имя класса
- значения атрибутов объекта:
    - name
    - description
    - price
    - quantity

---
### category

Создан класс <u>**Category**</u> с атрибутами:
- `name`: название категории
- `description`: описание категории
- `products` <span style="color:red">(приватный)</span>: список продуктов
- `category_count`: количество категорий
- `product_count`: количество продуктов

Реализован метод `add_product` для записи данных в приватный атрибут\
Информация по товару возвращается в виде строки:\
`Название продукта, _ руб. Остаток: _ шт.`

---
### product

Создан класс <u>**Product**</u> с атрибутами:
- `name`: название продукта
- `description`: описание продукта
- `price` <span style="color:red">(приватный)</span>: стоимость за 1 единицу
- `quantity`: количество продукта

Реализован класс-метод для создания нового продукта или обновления существующего

Добавлена проверка:\
цены:
- не может быть меньше или равна нулю
- понижение цены - только через дополнительное подтверждение

количество добавляемого товара - не может быть нулевым

---

### utils

Реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными.

---
### lawn_grass

Создан класс <u>**LawnGrass**</u> для представления газонной травы.\
Наследует атрибуты класса Product.

Дополнительные атрибуты:
- `country`: страна-производитель
- `germination_period`: срок прорастания
- `color`: цвет

---

### smartphone

Создан класс <u>**Smartphone**</u> для представления смартфонов.\
Наследует атрибуты класса Product.

Дополнительные атрибуты:

- `efficiency`: производительность
- `model`: модель
- `memory`: объем встроенной памяти 
- `color`: цвет

---

## Установка:

1. Клонируйте репозиторий:
```git clone git@github.com:E-Kryuger/OOP.git```
2. Установите зависимости:
```pip install -r requirements.txt```

## Примеры использования:

Примеры можно увидеть в тестировании каждого модуля.

## Тестирование:

Чтобы запустить тест надо написать команду `pytest` - она пройдётся по всем прописанным тестам.\
Если какой-то из тестов завершится ошибкой, то вы увидите где и какая ошибка произошла.

Чтобы увидеть покрытие тестами (***Code coverage***) надо написать команду `pytest --cov`
