import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO temps (celsius, fahrenheit) VALUES (?, ?)",
            (0, 32)
            )

cur.execute("INSERT INTO temps (celsius, fahrenheit) VALUES (?, ?)",
            (100, 212)
            )

connection.commit()
connection.close()