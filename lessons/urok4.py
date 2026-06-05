#Магические методы класса
class Test:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __add__(self, other):
        return self.value + other.value

    def __getitem__(self, item):
        return self.value[item]
    def __sub__(self, other):
        return self.value - other.value
    # def __add__(self, other):
    #     print(self.value)
    #     print(other.value)

# int_1 = Test(12)
# int_2 = Test(13)
# int_3 = int_1 + int_2
#
# print(int_3)

# obj_1 = Test('Just text')
# str_1 = "STR text"
#
# print(str_1)
# print(obj_1.value)

# my_int = 1123
# my_int2 = 123
# my_list = [1,2,34,5,6,7,]
# my_str = "text"
# int_2 = Test("13")
#
# print(my_int)
# print(my_list)
# print(my_str)
# print(int_2)

class Money:

    def connvert_money(self):
        pass

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
    def __add__(self, other):
        if self.currency != other.currency:
            return self.value + other.value
        else:
            print("Не можкем сложить разные валюты")