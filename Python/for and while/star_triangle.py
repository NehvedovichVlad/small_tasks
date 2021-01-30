"""
Дано нечетное натуральное число nn. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным nn в соответствии с примером:

*
**
***
****
***
**
*
Формат входных данных
На вход программе подается одно нечетное натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.

Sample Input 1:

3
Sample Output 1:

*
**
*
Sample Input 2:

5
Sample Output 2:

*
**
***
**
*
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
for i in range(num // 2):
    for j in range(i + 1):
        print('*', end='')
    print()
for k in range(num // 2 + 1):
    print('*', end='')
print()
for i in range(num // 2 + 1, 1, -1):
    for j in range(i - 1):
        print('*', end='')
    print()
# -------------------------------------------------------------------------------------------------

# 2)вариант
num = int(input())
count = 0
step = 1
for _ in range(num):
    if count == num//2 + 1:
        step = -1
    count += step
    print('*' * count)
# -------------------------------------------------------------------------------------------------

# 3)вариант
num = int(input())
for i in range(1, num + 1):
    print('*' * min(i, num - i + 1))