# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне[-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

list_numbers = []
n = abs(int(input("Введите число N: ")))
for k in range(-n, n+1):
    list_numbers.append(k)
print("Список чисел из диапазона [",-n, ",",n,"]:")
print(list_numbers)


position_1 = int(input("Введите номер первой позиции: "))
position_2 = int(input("Введите номер второй позиции: "))

if (0< position_1 <= 2*n+1) and (0 < position_2 <= 2*n+1):
    multi = int(list_numbers[position_1 - 1]) * int(list_numbers[position_2 - 1])
    print("Произведение элементов на указанных позициях равно ", multi)
else:
   print("Введенные позиции не соответствуют границам от 1 до ", 2*n+1)


