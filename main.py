from Tank import Paladin, Leviathan
from Attackers import Warrior, Thief
from Dice import Dice

def main():
    a_dice = Dice(6)
    
    char1 = Warrior("Michel", 20, 8, 3, Dice(6))
    char2 = Leviathan("Jason", 20, 8, 3, Dice(6))
    print(char1)
    print(char2)
    
    while(char1.is_alive() and char2.is_alive()):
        char1.attack(char2)
        char2.attack(char1)

if __name__ == "__main__":
   main()