# 3. Задайте список из n чисел, заполненный по формуле(1 + 1/n) ** n и выведите на экран их сумму.

list_1 = []
num = int(input())
for k in range(1, num+1):
    list_1.append(round((1+1/k)**k,3))
print(list_1)
sum=0
for k in list_1:
    sum+=k
print(sum)
