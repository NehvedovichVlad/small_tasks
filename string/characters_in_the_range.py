"""
Символы в диапазоне
На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения в диапазоне от aa до bb (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

Формат входных данных
На вход программе подается два натуральных числа, каждое на отдельное строке.

Формат выходных данных
Программа должна вывести текст в соотвествии с условием задачи.

Sample Input 1:

65
70
Sample Output 1:

A B C D E F
Sample Input 2:

97
110
Sample Output 2:

a b c d e f g h i j k l m n
Sample Input 3:

48
64
Sample Output 3:

0 1 2 3 4 5 6 7 8 9 : ; < = > ? @

"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')