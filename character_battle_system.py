def get_positive_integer(message):
        while True:
            try:
                value = int(input(message))
                if value <= 0:
                    print("Please enter a positive integer.")
                else:
                    return value
            except ValueError:
                print("Please enter a valid integer.")

def get_choice():
    while True:
        choice = input("Choose 1 for Attack or 2 for Special: ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")


class Character:
    def __init__(self, name, _health, damage):

        self.name = name
        
        if _health <= 0:
            raise ValueError("Health must be positive.")
        self._health = _health

        if damage <= 0:
            raise ValueError("Damage must be positive.")
        self.damage = damage
        self.special_uses = 2

    def show_health(self):
        print(f"{self.name}'s health: {self._health}")

    
    def take_damage(self, amount):
        if amount <=0:
            raise ValueError("Damage amount must be positive.")
        self._health -= amount
        if self._health < 0:
            self._health = 0
        if self._health == 0:
            print(f"{self.name} has been defeated!")

    def is_alive(self):
        return self._health > 0


class Warrior(Character):

    def attack(self, target):
        print("Warrior attacks with a sword!")
        target.take_damage(self.damage)

    def power_strike(self, target):
        if self.special_uses > 0:
            print("Warrior uses POWER STRIKE!")
            target.take_damage(self.damage * 2)
            self.special_uses -= 1
        else:
            print("Warrior has no special uses left!")

class Mage(Character):

    def attack(self, target):
        print("Mage attacks with magic!")
        target.take_damage(self.damage)

    def fireball(self, target):
        if self.special_uses > 0:
            print("Mage casts FIREBALL!")
            target.take_damage(self.damage * 3)
            self.special_uses -= 1
        else:
            print("Mage has no special uses left!")
        


warrior_name = input("Enter Warrior name: ")
warrior_health = get_positive_integer("Enter Warrior health: ")
warrior_damage = get_positive_integer("Enter Warrior attack damage: ")


mage_name = input("Enter Mage name: ")
mage_health = get_positive_integer("Enter Mage health: ")
mage_damage = get_positive_integer("Enter Mage attack damage: ")

warrior = Warrior(warrior_name, warrior_health, warrior_damage)
mage = Mage(mage_name, mage_health, mage_damage)

while warrior.is_alive() and mage.is_alive():

    choice = get_choice()

    if choice == "1":
        warrior.attack(mage)
    elif choice == "2":
        warrior.power_strike(mage)

    if mage.is_alive():
        choice = get_choice()

        if choice == "1":
            mage.attack(warrior)
        elif choice == "2":
            mage.fireball(warrior)

    warrior.show_health()
    mage.show_health()


if warrior.is_alive():
        print(f"{warrior.name} has won!")
else:
        print(f"{mage.name} has won!")
    



