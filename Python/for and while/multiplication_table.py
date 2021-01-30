"""
Таблица умножения
Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.

Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести таблицу умножения на введеное число.

Sample Input 1:

5
Sample Output 1:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант

n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)

# -------------------------------------------------------------------------------------------------

# 2)вариант

n = int(input())

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")