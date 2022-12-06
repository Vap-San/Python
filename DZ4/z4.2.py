# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in: 54
# out: [2, 3, 3, 3]

# in: 9990
# out: [2, 3, 3, 3, 5, 37]

# in:650
# out:[2, 5, 5, 13]

def factorization(number: int):
    prime_factors_list = []
    prime_number = 2
    copy_number = number
    while prime_number * prime_number <= number:
        if number % prime_number == 0:
            prime_factors_list.append(prime_number)
            number //= prime_number
        else:
            prime_number += 1
    prime_factors_list.append(number)

    print('{} = {}' .format(copy_number, prime_factors_list))
    return

number = int(input("Введите натуральное число: "))
factorization(number)
