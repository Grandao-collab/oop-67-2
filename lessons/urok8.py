import sqlite3

connect = sqlite3.connect('order.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        price INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')
connect.commit()

def create_data():
    users = [
        ('Ardager', 27),
        ('Oleg', 14),
        ('Slava', 33),
        ('John', 5),
    ]
    cursor.executemany(
        'INSERT INTO users(name, age) VALUES(?, ?)',
        users
    )
    connect.commit()
    print('Пользователи созданы!!')

def create_orders():
    orders = [
        ("Iphone 17 pro max", 1250, 1),
        ("Samsung s25 ultra", 900, 2),
        ("Pixel 10 pro", 1000, 4)
    ]
    cursor.executemany(
        'INSERT INTO orders(product, price, user_id) VALUES(?, ?, ?)',
        orders
    )
    connect.commit()
    print('Заказы созданы!!')

def get_user_order():
    cursor.execute('''
        SELECT users.name, orders.product 
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
    ''')
    data = cursor.fetchall()
    for i in data:
        print(f"name: {i[0]} product: {i[1]}")

create_data()
create_orders()
get_user_order()

connect.close()
