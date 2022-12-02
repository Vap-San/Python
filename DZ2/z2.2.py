# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

list_numbers = []
n = int(input("Введите число: "))
for k in range(1, n+1):
    product = 1
    for m in range(1,k+1):
        product *= m
    list_numbers.append(product)
print("Набор произведений чисел от 1 до ", n, " в виде списка:")
print(list_numbers)

