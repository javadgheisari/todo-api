import sqlite3

con = sqlite3.connect('todo.db')

c = con.cursor()
c.execute("DROP TABLE IF EXISTS users;")

# #computing values
# Col1, Col2, Col3, Col4, Byte = ('1234', 2, '5678', 'qwerty', 'bytestr')

c.execute("""CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY,
    email TEXT,
    name TEXT,
    password TEXT);""")


# # Insert data into A
# c.execute("""INSERT INTO A
#                 (Col1, Col2, Col3, Col4, Byte) VALUES (?, ?, ?, ?, ?)""",
#                 (Col1, Col2, Col3, Col4, Byte))

c.execute('SELECT * FROM users;')

print(c.fetchall())