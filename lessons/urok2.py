# Наследование
# Супер класс|Родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action!!"

# Дочерний класс
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
       super().__init__(name, lvl, hp)
       self.mp = mp

    def action(self):
        return f" this new action {self.name}"

    def cast_spell(self):
        return f"{self.name} cast spell!!"

Viego = Hero("Viego", 100, 1000)
Elisa_spider = MageHero("Elisa Spider", 100, 1000, 500)

# print(Viego.action())
# print(Elisa_spider.action())

class Fly:
    def f_action(self):
        return 'fly'

class Swim:
    def f_action(self):
        return 'swim'

class Animal:
    def f_action(self):
        return 'animal'

Rengar = Animal()

print(Rengar.f_action())
print(Rengar.f_action())
print(Rengar.f_action())

class A:
    def f_action(self):
        print ("A")
class B(A):
    def f_action(self):
        super().f_action()
        print ("B")

class C(A):
    def f_action(self):
        super().f_action()
        print ("C")

class D (B,C):
    def f_action(self):
        super().f_action()
        print ("D")

test_obj = D()

test_obj.f_action()
print(D.mro())