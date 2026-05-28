class Hero:

    def __init__(self, name, lvl, healthpoint, strength):
        self.name = name
        self.lvl = lvl
        self.healthpoint = healthpoint
        self.strength = strength

    def greet(self):
        print(f'{self.name}, уровень {self.lvl}')

    def attack(self):
        print(f'{self.name} наносит удар')
        self.strength -= 1

    def rest(self):
        print(f'{self.name} отдыхает...')
        self.healthpoint += 1

viego = Hero('Viego', 80, 100, 99,)
briar = Hero(' Briar', 60, 100, 80)

viego.greet()
viego.attack()
print(f'Сила после аттаки {viego.strength}:')
viego.rest()
print(f'Здоровье после отдыха {viego.healthpoint}')

print('-' * 40)

briar.greet()
briar.attack()
print(f'Сила после аттаки {briar.strength}:')
briar.rest()
print(f'Здоровье после отдыха {briar.healthpoint}')