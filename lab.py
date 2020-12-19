from abc import ABC, abstractmethod


class Charachter(ABC):


 print("Введите имя и уровень для каждого наследника:")


def attack(self):
    print("Attack")

def save_throw(self,attribute):
    print("Save")

def attack(self):
    print("Attack")

for number in range(10):
    pass
    for number1 in range(20):
        pass

@abstractmethod
def perk(self):
    pass


class Hero(Charachter):
    print("Please enter the name of your hero and his level ")
    name = input()
    level = int(input())
    max_hp = 10 + 14 * number * 8
    hp = max_hp
    armour_class = 15 + 10
    initiative_strength = number1 + 10
    print(max_hp)


    def perk(self):
         print("")


class Dragon(Charachter):
    print("Please enter the name of Dragon and his level ")
    name = input()
    level = int(input())
    def perk(self):
        print("Attack to hero ")



a = Hero()
a.perk()
b = Dragon()
b.perk()
