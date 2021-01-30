"""
Таблица-3
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 11 до nn в соответствии с примером.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 11 до nn.

Примечание. В конце строки может быть пробел.

Sample Input 1:

1
Sample Output 1:

1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
1 + 7 = 8
1 + 8 = 9
1 + 9 = 10
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()