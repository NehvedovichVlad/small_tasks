""""
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17
"""
# -------------------------------------------------------------------------------------------------

# 1)вариант

def get_next_prime(num):
    if num==1:
        return 2
    elif num==2:
        return 3
    else:
        for i in range(num+1,num+10):
            if i%2!=0 and i%3!=0:
                return i
n = int(input())

# вызываем функцию
print(get_next_prime(n))
# -------------------------------------------------------------------------------------------------

# 2)вариант

def get_next_prime(num):
    num += 1
    if 2 in [num, 2**num%num]:
        return num
    else:
        while not 2 in [num, 2**num%num]:
            num += 1
        return num

n = int(input())

print(get_next_prime(n))
# -------------------------------------------------------------------------------------------------

# 3)вариант

def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

n = int(input())

print(get_next_prime(n))