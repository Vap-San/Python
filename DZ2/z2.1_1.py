# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.


from decimal import Decimal
num = abs(Decimal(input("Введите число: "))).as_tuple()

print("Цифры числа\n", num.digits)
sum = 0
for digit in num.digits:
    sum += digit
print(sum)

