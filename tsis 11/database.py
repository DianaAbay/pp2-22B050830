import psycopg2
from config import host,user,password,db_name
username = str(input())
s_name = str(input())
number = int(input())
s = str(number)
string = ''
for i in s:
    if len(string) <= 3:
        string += i
connection = None
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
    cursor = connection.cursor()
    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE Phonebook(
    #         id serial PRIMARY KEY,
    #         name varchar(30) NOT NUll,
    #         surname varchar(30) NOT NULL,
    #         phone bigint NOT NULL
    #     )
    #     """)
    def records():
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Phonebook(name,surname,phone) VALUES ('Abylaikhan','Aman','87777777777');
            INSERT INTO Phonebook(name,surname,phone) VALUES ('Alikhan','Azirbayev','87776666666');
            INSERT INTO Phonebook(name,surname,phone) VALUES ('Daulet','Kenesov','87775555555');
            INSERT INTO Phonebook(name,surname,phone) VALUES ('Temirlan','Koibagar','87774444444');
        """)
    def update():
        cursor.execute("""SELECT * FROM Phonebook""")
        for i in cursor.fetchall():
            n = i[1]
            if n == username:
                return True
        return False
    def delete():
        cursor.execute("""DELETE FROM Phonebook WHERE name = %s """, (username,))
    # with connection.cursor() as cursor:
    #     cursor.execute("""DELETE FROM Phonebook WHERE id >= 21""")
    if update() == True:
        with connection.cursor() as cursor:
            cursor.execute("""
            UPDATE Phonebook
            SET phone = %s
            WHERE name = %s;""",
            (number, username))
    else:
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Phonebook(name,surname,phone) VALUES (%s,%s,%s)""", (username, s_name, number))
    if string == '8707' or string == '8777':
        records()
        update()
    else:
        print('Incorrect number!')
    delete()
finally:
    if connection is not None:
        connection.close()