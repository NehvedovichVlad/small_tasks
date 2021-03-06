"""
Без дубликатов
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.

Sample Input:

5
first
second
first
third
second
Sample Output:

first
second
third
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
dat = []
for i in range(num):
    a = input()
    dat.append(a)
y = sorted(set(dat), key=lambda d: dat.index(d))
for i in range(len(y)):
    print(y[i])
# -------------------------------------------------------------------------------------------------

# 2)вариант
dat = []
for _ in range(int(input())):
    el = input()
    if el not in dat:
        dat.append(el)
        print(el)