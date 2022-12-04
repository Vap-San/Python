# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988


from decimal import Decimal

def print_number_of_accuracy(number):
    accuracy = Decimal(input("Введите точность числа: "))
    print(number.quantize(Decimal(accuracy)))
    return

num = Decimal(input("Введите число: "))
print_number_of_accuracy(num)

