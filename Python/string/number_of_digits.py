"""
Количество цифр
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести количество цифр в данной строке.

Sample Input 1:

2k3.6/4c5c1v
Sample Output 1:

6
Sample Input 2:

2s6O3b4d5U1a
Sample Output 2:

6
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)