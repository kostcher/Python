# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    if n <= 0 or m <= 0 or m < n:
        return []

    fibonacci_row = [1, 1]

    for i in range(1, m - 1):
        fibonacci_row.append(
            fibonacci_row[i] + fibonacci_row[i - 1]
        )

    return fibonacci_row[n - 1:]


print(fibonacci(7, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


my_list = [8, 3, 6, 1, 0]


def bubble_sort(my_list):
    for i in range(0, len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                tmp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = tmp

    return my_list


print(bubble_sort(my_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def is_even(number):
    if number % 2 == 0:
        return True

    return False


my_list = [1, 2, 2, 5, 6, 8, 11]


def my_filter(func, iterated_obj):
    for value in iterated_obj:
        if not func(value):
            iterated_obj.remove(value)

    return iterated_obj


print(my_filter(is_even, my_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a, b, c, d = (1, 3), (4, 7), (2, 8), (-1, 4)


def is_vertex_parallelogram(a, b, c, d):
    import math

    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    dc = math.sqrt((c[0] - d[0])**2 + (c[1] - d[1])**2)

    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    bc = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)

    if ab == dc and ad == bc:
        return True

    return False


print(is_vertex_parallelogram(a, b, c, d))
