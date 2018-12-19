# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

my_list = []

my_list = [random.randint(-10, 10) for _ in range(10)]

square_my_list = [number**2 for number in my_list]

print(my_list)
print(square_my_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_fruits_list = [
    'apple',
    'orange',
    'avocado',
    'lemon',
    'apricot',
    'banana',
];

second_fruits_list = [
    'grapefruit',
    'grapes',
    'apple',
    'mango',
    'lime',
    'avocado',
    'lemon'
];


intersecting_fruits = [
    fruit
    for fruit in first_fruits_list
    if fruit in second_fruits_list
]

print(intersecting_fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = [random.randint(-10, 10) for _ in range(10)]

prepared_my_list = [
    number
    for number in my_list
    if number % 3 == 0 and number >= 0 and number % 4 != 0
]

print(my_list)
print(prepared_my_list)
