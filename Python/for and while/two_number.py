"""
Вторая цифра
Дано натуральное число n \, (n > 9)n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

Формат входных данных
На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

Формат выходных данных
Программа должна вывести его вторую (с начала) цифру.

Sample Input 1:

455672
Sample Output 1:

5
Sample Input 2:

59
Sample Output 2:

9
Sample Input 3:

123
Sample Output 3:

2
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
number = int(input())
n_number = 0
while number > 9:
    n_number = number % 10
    number = number // 10
print(n_number)

# -------------------------------------------------------------------------------------------------

# 2)вариант
num = input()
print(num[1])
