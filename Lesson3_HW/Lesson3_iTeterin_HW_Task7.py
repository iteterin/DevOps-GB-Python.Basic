# 7. Продолжить работу над заданием.
# В программу должна попадать строка из слов,
# разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Используйте написанную ранее
# функцию int_func().

def input_data():
    text = input("Введите текст из маленьких латинских букв: ")
    if text.islower():
        return text
    else:
        print("Вы ввели не верные данные. Попробуйте еще раз..")
        exit(1)


def int_func(text) -> str:
    result = list()
    text_list = text.split(' ')
    for word in text_list:
        word_list = list(word)
        word_list[0] = word_list[0].upper()
        word = ''.join(map(str, word_list))
        result.append(word)
    return ' '.join(map(str, result))


def main():
    lover_text = input_data()
    print(int_func(text=lover_text))


if __name__ == '__main__':
    print("Задание №6")
    main()
