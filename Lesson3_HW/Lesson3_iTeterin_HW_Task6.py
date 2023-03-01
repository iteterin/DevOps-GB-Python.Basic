# 6. Реализовать функцию int_func(), принимающую слова
# из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def input_data():
    text = input("Введите текст из маленьких латинских букв: ")
    if text.islower():
        return text
    else:
        print("Вы ввели не верные данные. Попробуйте еще раз..")
        exit(1)


def int_func(text) -> str:
    text_list = list(text)
    text_list[0] = text_list[0].upper()
    return ''.join(map(str, text_list))


def main():
    lover_text = input_data()
    print(int_func(text=lover_text))


if __name__ == '__main__':
    print("Задание №6")
    main()
