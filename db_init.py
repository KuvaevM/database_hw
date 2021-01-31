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
    mark INTEGER,
    time INTEGER
    )""")

    db.commit()
    db.close()


if __name__ == '__main__':
    init_table_marks()