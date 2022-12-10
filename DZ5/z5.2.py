# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# text_words.txt - обычный файл
# text_code_words.txt - закодированный файл


def rle_encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding


def rle_decode(s):
    decoding = ""
    count = ""
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ""
    print(decoding)
    return decoding


def rle_code_file(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "w", encoding="utf-8") as my_f_2:
        for line in my_f_1:
            my_f_2.write(rle_encode(line))


def rle_decode_file(name: str):
    with open(name, "r", encoding="utf-8") as my_f_1:
        for line in my_f_1:
            rle_decode(line)


rle_code_file("text_words.txt", "text_code_words.txt")
rle_decode_file("text_code_words.txt")
