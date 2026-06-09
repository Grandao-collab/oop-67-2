# # Статический метод (@staticmethod)
# # Используется, когда методу не нужны ни self, ни cls.
# # Обычная функция, но логически относящаяся к классу.
# class ServiceUser:
#
#     def __init__(self, value):
#         self.value = value
#
#     @staticmethod
#     def get_next_page_data(a, b):
#         return a + b
#
# # 2. Метод класса (@classmethod)
# # Получает доступ к самому классу через cls.
# # Используется для альтернативных конструкторов или работы с классом.
#
# class Bank:
#     # Атрибуты класса
#     name = Hero('Ardager', 100, 1000)
#
#     def __init__(self, value):
#         # Атрибуты экземпляра класса
#         self.value = value
#
#     def get_value(self):
#         return self.value
#
#     @classmethod
#     def get_name(cls):
#         return cls.name
#
#     @classmethod
#     def base_create(cls):
#         return cls("Base value")
#
# bank = Bank("Ardager")
# bank_1 = Bank.base_create()
#
# # print(bank.get_value())
# # print(bank.get_name())
# # print(bank_1.get_value())
# # print(bank_1.get_name())
#
# class Product:
#
#     def __init__(self, price):
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Цена может быть отрицательной!!")
#         self.__price = value
#
#     def get_price(self):
#         return self.__price
#
# iphone = Product(1250)
# #
# # print(iphone.price)
# # iphone.price = 200
# # print(iphone.price)
# # iphone.price = -200
#
#
# class User:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.last_name + " " + self.first_name
#
#
# ardager = User('Ardager', 'Kartanbekov')
#
# # print(ardager.full_name)
#
# # 1. Что такое декоратор?
# # Декоратор — это функция, которая принимает другую функцию как аргумент и
# # возвращает новую функцию, обычно обернутую в дополнительную функциональность.
from lessons.urok2 import test_obj


def simple_decorator(func):
    def wrapper():
        print("До выполнения!!!")
        func()
        print("после выполнения!!")
    return wrapper

@simple_decorator
def say_hello():
    print('Hello kitty!!')

# say_hello()

def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет {func.__name__}", func(name))

    return wrapper

@greeting_decorator
def greeting(name):
    return f'Как дела {name}?'

# greeting('Ardager')

def repeat(n=4):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat
def hello():
    print('Hello!!!')

# hello()


def class_decorator(clc):
    class NewClass(clc):
        def action(self):
            print('Newe action!!')
    return NewClass
@class_decorator
class OldClass:

    def action(self):
        print('Old action!!')

test_obj = OldClass()

test_obj.action()
