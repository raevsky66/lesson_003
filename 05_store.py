# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
goods_count_all = 0
goods_cost_all = 0
for good in goods:
    good_code = goods[good]
    good_count = 0
    good_cost = 0
    for good_in_store in store:
        if good_in_store == good_code:
             for dep in store[good_in_store]:
                 good_count += dep['quantity']
                 good_cost += good_count*dep['price']
    print(good, good_count,'шт', good_cost, 'руб')
    goods_count_all += good_count
    goods_cost_all += good_cost
print('Итого', goods_count_all,'шт', goods_cost_all, 'руб')