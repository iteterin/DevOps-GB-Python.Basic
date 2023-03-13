# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

def get_count_lines_words():
    lines = 0
    with open("./Lesson5/lesson5_Task2.txt", 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            lines += 1
            line_list = [x for x in line.split()]
            print(f"В строке № {lines} - {len(line_list)} слов.")
    print(f"Всего строк в файле - {lines}.")


def main():
    get_count_lines_words()


if __name__ == '__main__':
    print("Задание №2")
    main()
