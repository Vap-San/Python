# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import randint


def create_list(size):
    if size <1:
        print("Введено недопустимое количество элементов!")
        return []
    return [randint(0, 4*size) for i in range(size)]


def create_new_lis(list):
    result_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
    return(result_list)        


size = int(input("Введите количество элементов списка: "))
list_items = create_list(size)

print("Входной список: ", list_items)
print("Выходной список: ", create_new_lis(list_items))
