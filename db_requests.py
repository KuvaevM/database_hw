from db_init import get_connection


def subject_statistics(subject):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(f"""
        SELECT student_name, student_surname, mark FROM marks WHERE subject = ?
        """, (subject, ))
    res = cursor.fetchall()
    students, middle = change_data_type(res)

    db.commit()
    cursor.close()

    return students, middle


def group_statistics(group):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(f"""
        SELECT student_name, student_surname, mark FROM marks WHERE group_number = {group}
        """)
    res = cursor.fetchall()
    students, middle = change_data_type(res)

    db.commit()
    cursor.close()

    return students, middle


def change_data_type(data):
    students = []
    summary = 0
    for data_piece in data:
        students.append([data_piece[0], data_piece[1]])
        summary += data_piece[2]
    middle = summary / len(data)
    return students, middle


if __name__ == '__main__':
    a1, a2 = subject_statistics('Алгебра')
    b1, b2 = group_statistics(2)
    print(a1, a2)
    print(b1, b2)
