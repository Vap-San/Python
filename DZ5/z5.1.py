# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in: Number of words: 10
# out: # авб абв бав абв вба бав вба абв абв абв авб бав вба бав вба

# in: Number of words: 6
# out: ваб вба абв ваб бва абв ваб вба ваб бва

# in: Number of words: -1
# out: The data is incorrect

from random import choices
	
def create_list (k):
    words = ["".join(choices('абв', k=3)) for i in range(k)]
    print(f"Исходный текст: {words}")
    return words


def delete_word(lst,find_word):
    new_list = [i for i in lst if find_word not in i]
    print(f'Результат: {new_list}')
    return new_list


n = int(input("Введите количество слов: "))
if n>0:
    list_words = create_list(n)
    find_txt = str(input("Введите слово для удаления из текста: "))
    delete_word(list_words, find_txt)
else:
    print("Некоррректные данные!")
