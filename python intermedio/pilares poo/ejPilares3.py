#Multiple inheritance:
#Can be used to inherit from multiple classes, allowing a class to combine behaviors and attributes from more than one parent class.
#for example a character in a game that inherits abilities from both a "Warrior" class and a "Mage" class,
#this way he can use both physical attacks and magical spells.

class Warrior:
    def __init__(self, name):
        self.name = name


    def attack(self):
        print(f"{self.name} attacks with a sword!")
        return 


    def defend(self):
        print(f"{self.name} defends with a shield!")
        return


class Mage:
    def __init__(self, name):
        self.name = name


    def cast_spell(self):
        print(f"{self.name} casts a fireball!")
        return


    def teleport(self):
        print(f"{self.name} teleports to a safe location!")
        return


class BattleMage(Warrior, Mage):
    def __init__(self, name):
        self.name = name


    def fire_meele_attack(self):
        print(f"{self.name} attacks with a fireball and a sword!")


son_of_warrior_mage = BattleMage("Martheus")


#as we can see, the BattleMage class inherits from both the Warrior and Mage classes, making him able to use both types of attacks.
son_of_warrior_mage.attack()
son_of_warrior_mage.cast_spell()
son_of_warrior_mage.fire_meele_attack()


