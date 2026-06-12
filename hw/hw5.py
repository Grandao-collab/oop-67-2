import time

# 📌 Задание 1 — Проверка администратора
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("У вас нет доступа")
    return wrapper


@is_admin
def delete_video(user):
    print("Видео удалено")


# 📌 Задание 2 — Декоратор таймера
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start:.6f} секунд")
        return result
    return wrapper


@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


# 📌 Пример использования
if __name__ == "__main__":
    # Проверка администратора
    admin = User("King", "admin")
    user = User("Knight", "user")

    delete_video(admin)
    delete_video(user)

    # Таймер
    download_video()
