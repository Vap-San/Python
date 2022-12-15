# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


# n = int(input("Введите N>20: "))
# if n < 20:
#     print("Введено недопустимое значение!")
# else:
#     list = [i for i in range(20, n+1) if i % 20 == 0 or i % 21 == 0]
#     print("Числа кратные 20 или 21: ", list)


def create_list_20_21(right_margin):
    list = [i for i in range(20, right_margin+1) if i % 20 == 0 or i % 21 == 0]
    print("Числа кратные 20 или 21: ", list)


n = int(input("Введите N>20: "))
if n < 20:
    print("Введено недопустимое значение!")
else:
    create_list_20_21(n)
