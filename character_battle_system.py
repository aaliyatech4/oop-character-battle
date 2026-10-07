class Character:
    def __init__(self, name, _health):
        self.name = name
        self._health = _health

    def show_health(self):
        print(f"{self.name}'s health: {self._health}")

    
    def take_damage(self, amount):
        if amount <=0:
            raise ValueError("Damage amount must be positive.")
        self._health = self._health - amount
        if self._health < 0:
            self._health = 0
        if self._health == 0:
            print(f"{self.name} has been defeated!")

    def is_alive(self):
        return self._health > 0

class Warrior(Character):
    def attack(self, target, damage):
        print("Warrior attacks with a sword!")
        target.take_damage(damage)
        

class Mage(Character):
    def attack(self, target, damage):
        print("Mage attacks with magic!")
        target.take_damage(damage)
        


warrior_name = input("Enter Warrior name: ")
while True:
    try:
        warrior_health = int(input("Enter Warrior health: "))

        if warrior_health <= 0:
            print("Health must be a positive integer.")
        else:
            break

    except ValueError:
        print("Please enter a positive integer.")

while True:
    try:
        warrior_damage = int(input("Enter Warrior attack damage: "))

        if warrior_damage <= 0:
            print("Damage must be a positive integer.")
        else:
            break

    except ValueError:
        print("Please enter a positive integer.")

mage_name = input("Enter Mage name: ")
while True:
    try:
        mage_health = int(input("Enter Mage health: "))

        if mage_health <= 0:
            print("Health must be a positive integer.")
        else:
            break

    except ValueError:
        print("Please enter a positive integer.")
while True:
    try:
        mage_damage = int(input("Enter Mage attack damage: "))

        if mage_damage <= 0:
            print("Damage must be a positive integer.")
        else:
            break

    except ValueError:
        print("Please enter a positive integer.")

warrior = Warrior(warrior_name, warrior_health)
mage = Mage(mage_name, mage_health)


while warrior.is_alive() and mage.is_alive():

    warrior.attack(mage, warrior_damage)

    if mage.is_alive():
        mage.attack(warrior, mage_damage)

    if not warrior.is_alive():
        break

    warrior.show_health()
    mage.show_health()
    



