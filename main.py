import sqlite3


def connect():
    conn = sqlite3.connect('database.db')
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS famous_people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

    print("Table created successfully")


create_table()


def insert_data(single_data):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO famous_people(name, description) VALUES (?, ?)''', single_data)

    conn.commit()
    conn.close()

    print("Inserted single data successfully")


insert_data(("Steve Jobs", "Founder of Apple"))


def insert_data_many(many_data):
    conn = connect()
    cursor = conn.cursor()

    cursor.executemany('''INSERT INTO famous_people(name, description) VALUES (?, ?)''', many_data)

    conn.commit()
    conn.close()

    print("Inserted many data successfully")


insert_data_many([
    ("Michael Jackson", "Singer and Musician"),
    ("Steve Wozniak", "Creator of Personal Computer"),
])


def delete_data(id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM famous_people WHERE id = ?''', (id,))

    conn.commit()
    conn.close()

    print("Deleted successfully")


delete_data(2)
