"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из кубов указанных чисел.

Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

[1, 8, 27, 64, 125]
Sample Input 2:

2
-5
-2
Sample Output 2:

[-125, -8]
Sample Input 3:

1
100
Sample Output 3:

[1000000]
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
spisok = []
for i in range(num):
    a = int(input())
    spisok.append(a ** 3)
print(spisok)
# -------------------------------------------------------------------------------------------------

# 2)вариант
spisok = list()
for _ in range(int(input())):
    spisok.append(int(input()) ** 3)
print(spisok)

