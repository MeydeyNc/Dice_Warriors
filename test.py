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
        