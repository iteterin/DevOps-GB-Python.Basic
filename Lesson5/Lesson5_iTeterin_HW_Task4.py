# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

def read_data_from_file_and_translate(filename) -> list:
    translate_dict = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
    }
    translate_out_file = open(
        './Lesson5/lesson5_Task4_translate.txt', "w", encoding='utf-8')

    file_data = open(filename, "r", encoding='utf-8')
    content = file_data.readlines()
    for i in range(0, len(content)):
        line = content[i].split(' ')
        line[0] = translate_dict[line[0]]
        translate_out_file.write(" ".join(line))
    translate_out_file.close()


def main():
    data_from_file = read_data_from_file_and_translate(
        filename='./Lesson5/lesson5_Task4.txt')


if __name__ == '__main__':
    print("Задание №4")
    main()
