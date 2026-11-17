import sqlite3


def connect():
    conn = sqlite3.connect('database.db')
    return conn


# Задание 1
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            author TEXT NOT NULL,
            release_year INT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

    print("Table created successfully")


create_table()


# Задание 2
class Library:
    def insert_one(self, data):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO library (
                            title,
                            description,
                            author,
                            release_year
                        ) VALUES (?, ?, ?, ?)''', data)

        conn.commit()
        conn.close()

        print("Inserted single data successfully")


    def insert_many(self, data):
        conn = connect()
        cursor = conn.cursor()

        cursor.executemany('''INSERT INTO library (
                                title,
                                description,
                                author,
                                release_year
                            ) VALUES (?, ?, ?, ?)''', data)

        conn.commit()
        conn.close()

        print("Inserted many data successfully")


    def get_all_books(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM library""")
        books = cursor.fetchall()

        conn.close()

        return books


library = Library()

library.insert_many([
    (
        "1984",
        "Роман-антиутопия о тоталитарном обществе, где царят повсеместный контроль, слежка и манипуляция историей.",
        "Джордж Оруэлл",
        1949
    ),
    (
        "Мастер и Маргарита",
        "Философский роман о визите дьявола в Москву 1930-х годов, переплетенный с историей Иешуа и Понтия Пилата.",
        "Михаил Булгаков",
        1967
    ),
    (
        "Преступление и наказание",
        "Психологический роман о студенте Раскольникове, который решается на преступление ради проверки своей теории.",
        "Фёдор Достоевский",
        1866
    ),
    (
        "Три товарища",
        "Трогательная история о дружбе, любви и верности трех фронтовых друзей в период Великой депрессии в Германии.",
        "Эрих Мария Ремарк",
        1936
    ),
    (
        "Гарри Поттер и философский камень",
        "Начало культовой сказочной саги о мальчике-волшебнике, узнавшем о своем магическом происхождении.",
        "Джоан Роулинг",
        1997
    ),
    (
        "Маленький принц",
        "Философская сказка-притча о детской чистоте, дружбе, любви и ответственности за тех, кого мы приручили.",
        "Антуан де Сент-Экзюпери",
        1943
    ),
    (
        "Властелин колец: Братство Кольца",
        "Эпическое фэнтези о Средиземье, магии и опасном путешествии хоббита Фродо ради уничтожения Кольца Всевластия.",
        "Джон Р. Р. Толкин",
        1954
    ),
    (
        "Алхимик",
        "Притча-бестселлер о следовании за своей мечтой и поиске истинного жизненного предназначения.",
        "Пауло Коэльо",
        1988
    ),
    (
        "Марсианин",
        "Научно-фантастический роман об инженере, который случайно остался один на Марсе и борется за выживание.",
        "Энди Уир",
        2011
    )
])

library.insert_one((
    "Цветы для Элджернона",
    "Пронзительный научно-фантастический роман в жанре дневника об умственно отсталом парне, прошедшем экспериментальную операцию по увеличению интеллекта.",
    "Дниел Киз",
    1959
))

print(library.get_all_books())
