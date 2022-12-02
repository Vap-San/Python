# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import choices, randint

def genetate_list(count):
    list_numbers = choices(range(1, count*randint(1, count)), k=count)
    print(list_numbers)
    return list_numbers

def multiply_pairs(list_numbers):
    list_pair_of_numbers = []
    while len(list_numbers) > 1:
        list_pair_of_numbers.append(list_numbers[0]*list_numbers[-1])
        del list_numbers[0]
        del list_numbers[-1]
    if len(list_numbers) == 1:
        list_pair_of_numbers.append(list_numbers[0])
    return list_pair_of_numbers


print(multiply_pairs(genetate_list(int(input("Введите количество элементов списка: ")))))
