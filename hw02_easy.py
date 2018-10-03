# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']

for index, fruit in enumerate(fruits):
    print('%s.{:>10}'.format(fruit) % (index + 1))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

firstList = ['a', 'b', 'c', 'd', 'e', 'f']
secondList = ['t', 'a', 'j', 'u', 'e']

for index, secondListEl in enumerate(secondList):
    if secondListEl in firstList:
        firstList.remove(secondListEl)

print(firstList)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

numbers = []
numbersFormatted = []
cntNumbers = 10
i = 0

# Сгенерируем пустой массив
while i < cntNumbers:
    numbers.append(
        random.randint(0, 20)
    )
    i = i + 1


# Заполним новый массив, согласно правилам
for number in numbers:
    if number % 2 == 0:
        numbersFormatted.append(
            number / 4
        )
    else:
        numbersFormatted.append(
            number * 2
        )

print(numbers)
print(numbersFormatted)