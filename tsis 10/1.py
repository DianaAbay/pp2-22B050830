import psycopg2
from config import host,user,password,db_name
connection = None
name = str(input())
city = str(input())
number = int(input())
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("""ALTER TABLE PhoneBook ALTER COLUMN phone TYPE bigint;"""
        )
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE PhoneBook(
                id serial PRIMARY KEY,
                name varchar(30) NOT NULL,
                city varchar(30) NOT NULL,
                phone bigint NOT NULL
            )"""
        )
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO PhoneBook (name, city, phone) VALUES ('Abylaikhan', 'Almaty', '87777777777');
            INSERT INTO PhoneBook (name, city, phone) VALUES ('Alikhan', 'Aqtau', '87776666666');
            INSERT INTO PhoneBook (name, city, phone) VALUES ('Olzhas', 'Shymkent', '87775555555');
            INSERT INTO PhoneBook (name, city, phone) VALUES ('Aibol', 'Taraz', '87774444444');
            INSERT INTO PhoneBook (name, city, phone) VALUES ('Zhanbolat', 'Astana', '87773333333');
            """
        )
    with connection.cursor() as cursor:
        cursor.execute("""DELETE FROM PhoneBook WHERE id = 8""")
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO PhoneBook (name, city, phone) VALUES (%s, %s, %s)""", (name,city,number))
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
    with connection.cursor() as cursor:
        cursor.execute("""UPDATE PhoneBook
        SET name = 'Daulet'
        WHERE id = 10""")
    with connection.cursor() as cursor:
        cursor.execute("""DELETE FROM PhoneBook WHERE name = 'Daulet'""")
finally:
    if connection is not None:
        connection.close()
        print("PostgreSQL connection closed")
        