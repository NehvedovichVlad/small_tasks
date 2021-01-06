"""
Список делителей
На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.

Sample Input 1:

17
Sample Output 1:

[1, 17]
Sample Input 2:

25
Sample Output 2:

[1, 5, 25]
Sample Input 3:

36
Sample Output 3:

[1, 2, 3, 4, 6, 9, 12, 18, 36]
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
spisok = []
for i in range(1, num + 1):
    if num % i == 0:
        spisok.append(i)
print(spisok)

