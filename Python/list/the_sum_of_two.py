"""
Суммы двух
На вход программе подается натуральное число n \ge 2n≥2, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел.

Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

[3, 5, 7, 9]
Sample Input 2:

2
10
9
Sample Output 2:

[19]
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
spisok = []
spisok2 = []
gg = 0
for i in range(1, num + 1):
    gg = int(input())
    spisok.append(gg)
for j in range(1, num):
    s = spisok[j - 1] + spisok[j]
    spisok2.append(s)
print(spisok2)
# -------------------------------------------------------------------------------------------------

# 2)вариант
spisok1, spisok2 = int(input()), int(input())
lst = []
for _ in range(spisok1 - 1):
    gg = int(input())
    lst.append(spisok2 + gg)
    spisok2 = gg
print(lst)