# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import choices, randint

def generate_list(count):
    list_numbers = choices(range(1, count*randint(1,count)), k=count)
    print(list_numbers)
    return list_numbers


def sum_numbers_on_odd_positions(list_numbers):
    sum=0
    for i in range(0, len(list_numbers),2):
        sum += list_numbers[i]
    return sum


print(sum_numbers_on_odd_positions(generate_list(int(input("Введите количество элементов списка: ")))))
