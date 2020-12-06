"""Звездный треугольник
На вход программе подается натуральное число n \, (n \ge 2)n(n≥2) – катет прямоугольного равнобедренного треугольника.

Напишите программу, которая выводит звездный треугольник в соответствии с примером.

Формат входных данных
На вход программе подается одно натуральное число n \, (n \ge 2)n(n≥2).

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием задачи.

Sample Input 1:

3
Sample Output 1:

***
**
*
Sample Input 2:

11
Sample Output 2:

***********
**********
*********
********
*******
******
*****
****
***
**
*
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант

n = int(input())
for i in range(n):
    print('*'*(n-i))

# -------------------------------------------------------------------------------------------------

# 2)вариант

[print('*' * i) for i in range(int(input()), 0, -1)]