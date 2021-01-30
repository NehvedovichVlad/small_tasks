"""
Таблица-2
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу размером n \times 5n×5, где в ii-ой строке указано число ii (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n \times 5n×5 в соответствии с условием.

Примечание. В конце строки может быть пробел.

Sample Input 1:

3
Sample Output 1:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
num = int(input())
for i in range(1,num+1):
    for j in range(5):
        print(i, end=' ')
    print()
# -------------------------------------------------------------------------------------------------

# 2)вариант
[print(*[i + 1] * 5) for i in range(int(input()))]