"""
Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

Формат входных данных
На вход программе подаются натуральное число n >= 2, а затем nn различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два наибольших числа, каждое на отдельной строке.

Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

5
4
Sample Input 2:

8
9
7
5
4
3
2
78
1
Sample Output 2:

78
9
"""
# 1)вариант

n = int(input())
max1 = 1
max2 = 0
for i in range(n):
    a = int(input())
    if a > max2:
        max2 = a
    if max2 >= max1:
        max2, max1 = max1, max2
print(max1, max2, sep='\n')


