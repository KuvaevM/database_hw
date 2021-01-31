from db_init import get_connection


def read_data_file(name):
    """Метод считывает словарь словоформ"""
    with open(name) as f:
        number_of_string = 0
        text_in_dictionary = f.read()
        strings = text_in_dictionary.split('\n')
        if strings[len(strings) - 1] == '':  # Удаляем последний элемент с пустой строкой
            strings.pop()
        for line in strings:
            data = line.split(',')
            marks_filling(data)


def marks_filling(data):
    db = get_connection()
    print(data)

    db.execute(f""" INSERT INTO marks
                            VALUES(?, ?, ?, ?, ?, strftime('%s',?))""",
               (data[1], data[3], data[4], int(data[5]), int(data[0]), data[2]))
    db.commit()
    db.close()


if __name__ == '__main__':
    read_data_file('test_odict1.csv')