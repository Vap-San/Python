from decimal import Decimal
from logg import logging


def choice_type_numbers():
    while True:
        type_number = input("Выберите тип числа:"
                            "\n1 - рациональные"
                            "\n2 - комплексные"
                            "\n================"
                            "\n-->  ")
        if type_number.isdigit() and int(type_number) in range(1, 3):
            break
    return type_number


def get_value_q():
    while True:
        value = input('Введите рациональное число: ')
        try:
            value = Decimal(value)
            break
        except:
            logging.warning("Error! Incorrect input")
            print("Ошибка! Введено не числовое значение!")
    return value


def get_value_complex():
    while True:
        value = input('Введите комплексное число вида a+bj: ')
        try:
            value = complex(value)
            break
        except:
            logging.warning("Error! Incorrect input")
            print("Ошибка! Введено не числовое значение!")
    return value


def get_operator():
    while True:
        oper = input("Выберите операцию:"
                     "\n1 - sum"
                     "\n2 - sub"
                     "\n3 - mult"
                     "\n4 - div"
                     "\n=========="
                     "\n-->  ")
        if oper.isdigit() and int(oper) in range(1, 5):
            break
    return oper


def get_result(res):
    print(f'Результат: {res}')
