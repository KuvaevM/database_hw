from db_init import get_connection


def subject_statistics(subject):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(f"""
        SELECT student_name, student_surname, mark FROM marks WHERE subject = ?
        """, (subject, ))
    res = cursor.fetchall()
    db.commit()
    cursor.close()
    return res


def group_statistics(group):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(f"""
        SELECT student_name, student_surname, mark FROM marks WHERE group_number = {group}
        """)
    res = cursor.fetchall()
    db.commit()
    cursor.close()
    return res

if __name__ == '__main__':
    a = subject_statistics('Алгебра')
    b = group_statistics(2)
    print(a)
    print(b)