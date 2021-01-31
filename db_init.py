import sqlite3


def get_connection():
    """Функция устанавливает соединение с базой данных"""
    __connection = sqlite3.connect('database/education.db')
    return __connection


def init_table_marks():
    """Функция создает таблицу marks в базе данных, если ее еще нет"""
    db = get_connection()

    db.execute(""" CREATE TABLE IF NOT EXISTS marks( 
    subject TEXT,
    student_name TEXT,
    student_surname TEXT,
    group_number INTEGER,
    mark INTEGER,
    time INTEGER
    )""")

    db.commit()
    db.close()

def init_table_subjects():
    """Функция создает таблицу marks в базе данных, если ее еще нет"""
    db = get_connection()

    db.execute(""" CREATE TABLE IF NOT EXISTS subjects( 
    subject TEXT,
    teacher_name TEXT,
    teacher_surname TEXT
    )""")

    db.commit()
    db.close()


def init_table_students():
    """Функция создает таблицу marks в базе данных, если ее еще нет"""
    db = get_connection()

    db.execute(""" CREATE TABLE IF NOT EXISTS students( 
    student_name TEXT,
    student_surname TEXT,
    country TEXT,
    group_number INTEGER,
    birthday INTEGER
    )""")

    db.commit()
    db.close()


if __name__ == '__main__':
    init_table_marks()
    init_table_subjects()
    init_table_students()