"""
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
"""


# -----------------------------------------------------------------------------------------

# 1) вариант

# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep="")


# считываем данные
name, surname, patronymic = input().title(), input().title(), input().title(),

# вызываем функцию
print_fio(name, surname, patronymic)
# ----------------------------------------------------------------------------------------


# 2)вариант

def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


name, surname, patronymic = input(), input(), input(),
print_fio(name, surname, patronymic)
