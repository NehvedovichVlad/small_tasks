"""Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента
 номер месяца и возвращает количество дней в данном месяце.

Примечание 1. Гаранитируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

Примечание 2. Считайте, что год является невисокосным."""


# -------------------------------------------------------------------------------------------------


# 1)вариант
def get_days(month):
    if month == 2:
        return 28
    elif month in [2, 4, 6, 9, 11]:
        return 30
    else:
        return 31


print(get_days(int(input())))


# -------------------------------------------------------------------------------------------------
# 2)вариант
# объявление функции
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
