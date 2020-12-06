"""Напишите функцию convert_to_miles(km),
которая принимает в качестве аргумента расстояние в километрах
и возвращает расстояние в милях.
 Формула для преобразования: мили = километры * 0.6214."""


# -------------------------------------------------------------------------------------------
# 1) вариант

# объявление функции
def convert_to_miles(km):
    return km * 0.6214


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
# -------------------------------------------------------------------------------------------

# 2) вариант
# объявление функции
convert_to_miles = lambda km: km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))