from abc import ABC, abstractmethod


class Hero(ABC):

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"{self.name}, уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):

    def attack(self):
        print(f"{self.name} атакует мечом! Демасия!")


class Mage(Hero):

    def attack(self):
        print(f"{self.name} использует магию света")


class Assassin(Hero):

    def attack(self):
        print(f"{self.name} атакует из тени")


# Персонажи из League of Legends
warrior = Warrior("Гарен", 10, 100, 20)
mage = Mage("Люкс", 12, 80, 30)
assassin = Assassin("Зед", 11, 90, 25)

# Проверка работы
warrior.greet()
warrior.attack()
warrior.rest()
print("-" * 30)

mage.greet()
mage.attack()
mage.rest()
print("-" * 30)

assassin.greet()
assassin.attack()
assassin.rest()