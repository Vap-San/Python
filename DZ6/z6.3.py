# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# in: Иван, Мария, Петр, Илья, Марина, Петр, Алина, Бибочка, Solomon, Stepan
# out: {'S': ['Solomon', 'Stepan'], 'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def input_str():
    words = input("Введите список имен через запятую: ").split(', ')
    words.sort()
    print("Отсортированный список: ", words)
    return words


def create_dictionary(words: list):
    dic = {}
    for word in words:
        key = word[0]
        if key in dic.keys():
            dic[key].append(word)
        else:
            dic[key] = [word]
    print("Словарь: ", dic)
    return (dic)


create_dictionary(input_str())
