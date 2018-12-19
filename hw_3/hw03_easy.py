# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, n_digits):
    number = number * (10 ** n_digits)

    if float(number) - int(number) > 0.5:
        number = number // 1 + 1
    else:
        number = number // 1

    return number / (10 ** n_digits)


print(my_round(2.723, 0))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def is_ticket_happy(ticket):
    ticket = list(map(int, str(ticket)))

    if len(ticket) != 6:
        return False

    if sum(ticket[:3]) != sum(ticket[3:]):
        return False

    return True


print(is_ticket_happy(123123))
