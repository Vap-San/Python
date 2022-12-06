# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.
# in: 7
# out:[4, 5, 3, 3, 4, 1, 2] [5, 1, 2]

# in:-1
# out: Negative value of the number of numbers! []

# in:10
# out: [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] [6, 2, 3, 0, 9]

from random import randint


def create_list(size):
    if size >-1:
        return [randint(0, size-1) for i in range(size)]
    else:
        print("Введено отрицательное количество элементов!")
        return []


def get_list_unique_items(list):
    list_unique = []
    for i in list:
        if list.count(i)==1:
            list_unique.append(i)
    return list_unique

size=int(input("Введите количество элементов списка: "))
list_items = create_list(size)
print("Входной список: ", list_items)
print("Выходной список: ", get_list_unique_items(list_items))
