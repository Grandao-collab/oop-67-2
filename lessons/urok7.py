import sqlite3


# A4
connect = sqlite3.connect('user.db')
# Рука и карандаш
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()



# CRUD - Create - Read - Update - Delete

def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    )
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    connect.commit()
    print("Пользователь создан!!")

# create_user("Ardager", 10, "кушать-спать-играть")
# create_user("KArtan", 10, "кушать-спать-играть")
# create_user("Oleg", 10, "кушать-спать-играть")
# create_user("Slava", 10, "кушать-спать-играть")


def get_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)

# get_users()

def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (name, rowid)
    )
    connect.commit()
    print('Пользователь обнавлен')

update_user('Oleg', 2)

def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print('Пользователь удален!!')

# delete_user(3)