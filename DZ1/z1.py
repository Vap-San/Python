#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
#*Пример:*
#
#- 6 -> да
#- 7 -> да
#- 1 -> нет

num = int(input())
if 5 < num < 8:
    print("Да")
elif 0 < num < 6:
    print("Нет")
else:
    print("Такого дня в неделе нет")