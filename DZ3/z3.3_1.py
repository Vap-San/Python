# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def dec_to_bin(number):
    list_digits = []
    bin_digit = 0
    while number > 0:
        bin_digit = number % 2
        list_digits.insert(0, bin_digit)
        number //=2 
    return list_digits



n = int(input("Введите целое число: "))
list_bin_digits = dec_to_bin(n)
print(*list_bin_digits, sep="")
