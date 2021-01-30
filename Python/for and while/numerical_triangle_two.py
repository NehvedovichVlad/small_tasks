"""
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.

Sample Input:

3
Sample Output:

1
2 3
4 5 6
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант

num = int(input())
count = 0
for i in range(1, num + 1):
    for j in range(i):
        count += 1
        print(count, end=' ')
    print()
# -------------------------------------------------------------------------------------------------

# 2)вариант
num = 1
for i in range(1, int(input())+1):
    print(' '.join(map(str, [j for j in range(num, num + i)])))
    num += i