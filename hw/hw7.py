import sqlite3

def init_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_product(name, price, quantity):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                   (name, price, quantity))
    conn.commit()
    conn.close()

def read_products():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product(id, price):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
    conn.commit()
    conn.close()


def delete_product(id):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

    create_product("Телефон", 15000, 10)
    create_product("Ноутбук", 55000, 5)
    create_product("Наушники", 2500, 20)

    print("Все товары:")
    for row in read_products():
        print(row)

    update_product(1, 17000)

    delete_product(2)

    print("\n После изменений:")
    for row in read_products():
        print(row)
