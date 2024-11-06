import sqlite3


def execute_query(sql_query: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql_query)
        return cur.fetchall()


def get_sql(filepath: str) -> str:
    with open(filepath, 'r') as f:
        sql = f.read()

    return sql


def display_table(data):
    max_lengths = [max(len(str(item)) for item in column) for column in zip(*data)]

    for row in data:
        print(" | ".join(f"{str(cell):<{max_lengths[i]}}" for i, cell in enumerate(row)))


if __name__ == '__main__':
    print("Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    display_table(execute_query(get_sql('queries/query_1.sql')))
    print('~'*40)

    print("Знайти студента із найвищим середнім балом з певного предмета.")
    display_table(execute_query(get_sql('queries/query_2.sql')))
    print('~'*40)

    print("Знайти середній бал у групах з певного предмета.")
    display_table(execute_query(get_sql('queries/query_3.sql')))
    print('~'*40)

    print("Знайти середній бал на потоці (по всій таблиці оцінок).")
    display_table(execute_query(get_sql('queries/query_4.sql')))
    print('~'*40)

    print("Знайти які курси читає певний викладач.")
    display_table(execute_query(get_sql('queries/query_5.sql')))
    print('~' * 40)

    print("Знайти список студентів у певній групі.")
    display_table(execute_query(get_sql('queries/query_6.sql')))
    print('~' * 40)

    print("Знайти оцінки студентів у окремій групі з певного предмета.")
    display_table(execute_query(get_sql('queries/query_7.sql')))
    print('~' * 40)

    print("Знайти середній бал, який ставить певний викладач зі своїх предметів.")
    display_table(execute_query(get_sql('queries/query_8.sql')))
    print('~' * 40)

    print("Знайти список курсів, які відвідує студент.")
    display_table(execute_query(get_sql('queries/query_9.sql')))
    print('~' * 40)

    print("Список курсів, які певному студенту читає певний викладач.")
    display_table(execute_query(get_sql('queries/query_10.sql')))
    print('~' * 40)
