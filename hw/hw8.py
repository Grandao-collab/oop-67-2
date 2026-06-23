import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
''')

users = [
    ("Ardager",),
    ("Oleg",),
    ("Slava",),
    ("John",),
    ("Tilek",)
]
cursor.executemany("INSERT INTO users(name) VALUES(?)", users)

movies = [
    ("Inception", "Sci-Fi"),
    ("Titanic", "Drama"),
    ("The Matrix", "Sci-Fi"),
    ("Interstellar", "Sci-Fi"),
    ("Gladiator", "Action"),
    ("Avatar", "Fantasy"),          # фильм без отзывов
    ("The Godfather", "Crime"),     # фильм без отзывов
    ("Shrek", "Animation")          # фильм без отзывов
]
cursor.executemany("INSERT INTO movies(title, genre) VALUES(?, ?)", movies)

reviews = [
    (1, 1, 9),
    (2, 1, 8),
    (3, 2, 10),
    (4, 2, 7),
    (5, 3, 6),
    (1, 4, 9),
    (2, 4, 10),
    (3, 5, 8),
    (4, 5, 9),
    (5, 5, 7),
    (1, 3, 10),
    (2, 3, 9)
]
cursor.executemany("INSERT INTO reviews(user_id, movie_id, rating) VALUES(?, ?, ?)", reviews)

conn.commit()

print("JOIN: имя пользователя + фильм + оценка")
cursor.execute('''
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
''')
for row in cursor.fetchall():
    print(row)

print("\nJOIN: все фильмы (даже без отзывов)")
cursor.execute('''
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
''')
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT AVG(rating) FROM reviews")
print("\nСредняя оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])

conn.close()
