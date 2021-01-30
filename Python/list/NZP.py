"""
Negatives, Zeros and Positives
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

7
3
-4
1
0
-1
0
-2
Sample Output 1:

-4
-1
-2
0
0
3
1
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
s = []
for i in range(num):
    stroka = int(input())
    s.append(stroka)
for j in range(num):
    if s[j] < 0:
        print(s[j])
for j in range(num):
    if s[j] == 0:
        print(s[j])
for j in range(num):
    if s[j] > 0:
        print(s[j])
# -------------------------------------------------------------------------------------------------

# 2)вариант
a, b, c = list(), list(), list()
for _ in range(int(input())):
    n = int(input())
    if n > 0:
        a.append(n)
    elif n < 0:
        b.append(n)
    elif n == 0:
        c.append(n)
print(*b, sep='\n')
print(*c, sep='\n')
print(*a, sep='\n')