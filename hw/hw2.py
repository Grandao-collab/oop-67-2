import random

class Hero:
    def __init__(self, name, level=1, health=100, strength=10):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, уровень {self.level}.")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        self.health += 20
        print(f"{self.name} отдыхает и восстанавливает здоровье до {self.health}.")


class Warrior(Hero):
    def __init__(self, name, level=1, health=120, strength=15, stamina=80):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level=1, health=90, strength=12, mana=100):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


# Заменили Assassin на Archer (Стрелок)
class Archer(Hero):
    def __init__(self, name, level=1, health=95, strength=14, accuracy=90):
        super().__init__(name, level, health, strength)  # Исправлено на __init__
        self.accuracy = accuracy  # Вместо скрытности (stealth) теперь меткость (accuracy)

    def attack(self):
        print(f"{self.name} стреляет из лука!")


def determine_winner(player, enemy):
    # Обновили правила: Воин побеждает Стрелка, Стрелок побеждает Мага, Маг побеждает Воина
    rules = {
        'Warrior': 'Archer',
        'Archer': 'Mage',
        'Mage': 'Warrior',
    }

    if player.name == enemy.name:
        return 'Ничья!'

    if rules[player.name] == enemy.name:
        return f'{player.name} победил!'

    return f'{enemy.name} победил!'


def main():
    warrior = Warrior('Warrior', level=5, stamina=90)
    mage = Mage('Mage', level=5, mana=120)
    archer = Archer('Archer', level=5, accuracy=95)  # Создаем Стрелка

    heroes = {
        'warrior': warrior,
        'mage': mage,
        'archer': archer,
    }

    print('Созданы герои:')
    for hero in heroes.values():
        hero.greet()
        hero.attack()
        print()

    choice = input('Выберите героя:\nWarrior / Mage / Archer\nВаш выбор: ').strip().lower()
    if choice not in heroes:
        print('Неверный выбор героя. Пожалуйста, выберите Warrior, Mage или Archer.')
        return

    player = heroes[choice]
    opponents = [hero for key, hero in heroes.items() if key != choice]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}")
    print()

    result = determine_winner(player, enemy)
    print(result)


# Исправлено на правильный синтаксис Python
if __name__ == '__main__':
    main()