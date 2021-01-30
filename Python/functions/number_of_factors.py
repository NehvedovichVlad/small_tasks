"""Напишите функцию number_of_factors(num),
 принимающую в качестве аргумента число и
 возвращающую количество делителей данного числа."""


# -------------------------------------------------------------------------------------------------

# 1)вариант

def number_of_factors(num):
    # pass
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    return total


n = int(input())

# вызываем функцию
print(number_of_factors(n))


# -------------------------------------------------------------------------------------------------

# 2)вариант

def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])

n = int(input())

# вызываем функцию
print(number_of_factors(n))
