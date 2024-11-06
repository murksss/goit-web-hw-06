import calendar
from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 4


def generate_random_date(year):
    month = randint(1, 12)
    days_in_month = calendar.monthrange(year, month)[1]
    day = randint(1, days_in_month)
    return datetime(year, month, day).date().isoformat()


def generate_fake_data(number_of_gropus,
                       number_of_students,
                       number_of_teachers,
                       ) -> tuple:
    """ generate fake data list """

    fake_groups = list()
    fake_students = list()
    fake_teachers = list()

    fake = faker.Faker()

    # create groups list
    for _ in range(number_of_gropus):
        fake_groups.append(fake.unique.lexify(text="?????"))

    # create students list
    for _ in range(number_of_students):
        fake_students.append(fake.unique.name())

    # create subjects list
    fake_subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Art', 'Music']

    # create teachers list
    for _ in range(number_of_teachers):
        fake_teachers.append(fake.unique.name())

    fake_marks = range(1, 13)

    return fake_groups, fake_students, fake_subjects, fake_teachers, fake_marks


def prepare_fake_data(groups, students, subjects, teachers, marks) -> tuple:
    for_groups = list()
    for group in groups:
        for_groups.append((group, ))

    for_students = list()
    for student in students:
        for_students.append((student, randint(1, len(groups))))

    for_teachers = list()
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = list()
    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers))))

    for_marks = list()
    for _ in students:
        for _ in range(randint(13, 21)):
            mark_date = generate_random_date(2024)
            for_marks.append((
                choice(marks),
                mark_date,
                randint(1, len(students)),
                randint(1, len(subjects))
            ))

    return for_groups, for_students, for_subjects, for_teachers, for_marks


def insert_data(groups, students, subjects, teachers, marks) -> None:
    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(student_name, fk_group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                                        VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, fk_teacher_id)
                                VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_marks = """INSERT INTO marks(mark, date, fk_student_id, fk_subject_id)
                                                VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


if __name__ == "__main__":
    groups, students, subjects, teachers, marks = prepare_fake_data(
        *generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS)
    )
    insert_data(groups, students, subjects, teachers, marks)