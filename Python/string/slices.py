"""
Делаем срезы 1
На вход программе подается одна строка. Напишите программу, которая выводит:

общее количество символов в строке;
исходную строку повторенную 3 раза;
первый символ строки;
первые три символа строки;
последние три символа строки;
строку в обратном порядке;
строку с удаленным первым и последним символом.
Формат входных данных
На вход программе подается одна строка, длина которой больше 3 символов.

Формат выходных данных
Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

Sample Input:

abcdefghijklmnopqrstuvwxyz
Sample Output:

26
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
a
abc
xyz
zyxwvutsrqponmlkjihgfedcba
bcdefghijklmnopqrstuvwxy
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант
stroka = input()
total = 0
for i in range(len(stroka)):
    total += 1
print(total)
print(stroka * 3)
print(stroka[0])
print(stroka[:3])
print(stroka[-3:])
print(stroka[::-1])
print(stroka[1:-1])
