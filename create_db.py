import sqlite3
from contextlib import contextmanager
from sqlite3 import Error


@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    groups_sql = """
    CREATE TABLE groups (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name CHAR(5) UNIQUE NOT NULL
    );
    """

    students_sql = """
    CREATE TABLE students (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name VARCHAR(30) NOT NULL,
        fk_group_id INTEGER NOT NULL,
        FOREIGN KEY(fk_group_id) REFERENCES groups (pk_id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
    );
    """

    teachers_sql = """
    CREATE TABLE teachers (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name VARCHAR(30) NOT NULL
    );
    """

    subjects_sql = """
    CREATE TABLE subjects (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name VARCHAR(30) NOT NULL,
        fk_teacher_id INTEGER NOT NULL,
        FOREIGN KEY(fk_teacher_id) REFERENCES teachers (pk_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """

    marks_sql = """
    CREATE TABLE marks (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mark INTEGER NOT NULL,
        date DATE NOT NULL,
        fk_student_id INTEGER NOT NULL,
        fk_subject_id INTEGER NOT NULL,
        FOREIGN KEY(fk_student_id) REFERENCES students (pk_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY(fk_subject_id) REFERENCES subjects (pk_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """

    database = './university.db'

    with create_connection(database) as conn:
        if conn is not None:
            # create groups table
            create_table(conn, groups_sql)
            # create students table
            create_table(conn, students_sql)
            # create teachers table
            create_table(conn, teachers_sql)
            # create subjects table
            create_table(conn, subjects_sql)
            # create marks table
            create_table(conn, marks_sql)
        else:
            print("Error! cannot create the database connection.")
