from Attackers import *

if __name__ == "__main__":
    a_dice = Dice(6)

    character1 = Thief("Guerrier", Dice(6))
    character2 = Mage("Lisa", Dice(6))
    print(character1)
    print(character2)

    
    while(character1.is_alive() and character2.is_alive()):
        character1.attack(character2)
        character2.attack(character1)
        
from Tank import Paladin, Leviathan, Guardian, Enforcer, Shield_Master
from Attackers import Warrior, Thief
from Dice import Dice

def main():
    a_dice = Dice(6)
    
    
    
    char1 = Shield_Master("Shield_master", Dice(6))
    char2 = Warrior("Warrior", Dice(6))
    
    print(char1)
    print(char2)
    
    while(char1.is_alive() and char2.is_alive()):
        char1.attack(char2)
        char2.attack(char1)

if __name__ == "__main__":
   main()