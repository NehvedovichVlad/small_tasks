"""Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.
*
**
***
****
*****
****
***
**
*
"""


# -------------------------------------------------------------------------------------
# 1) вариант

# объявление функции
def draw_triangle(fill, base):
    # pass
    for i in range(1, base + 1):
        if i <= base // 2:
            print(fill * i)
    print(fill * (base // 2 + 1))
    for i in range(base + 1, 0, -1):
        if i <= base // 2:
            print(fill * i)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# ----------------------------------------------------------------------------------------


# 2) вариант
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)