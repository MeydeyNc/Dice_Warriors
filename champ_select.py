from Attackers import Samurai, Berserker, Mage, Thief, Warrior
from Tank import Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian
from rich import print

# Beta

def select_characters(character_type: str):
    if character_type.lower() == "tank":
        character_classes = [Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian]
    elif character_type.lower() == "attacker":
        character_classes = [Samurai, Berserker, Mage, Thief, Warrior]
    else:
        raise ValueError("character_type expected !")

    print(f"Choisissez les numéros des personnages que vous souhaitez ajouter à la liste (séparés par des espaces):")
    
    for i, character_class in enumerate(character_classes, start=1):
        print(f"{i}. {character_class.__name__}")

    choices = input().split()

    chosen_characters = []
    invalid_choices = False

    for choice in choices:
        try:
            index = int(choice) - 1
            if 0 <= index < len(character_classes):
                chosen_characters.append(character_classes[index])
            else:
                print(f"Choix invalide : {choice}. Ignoré.")
                invalid_choices = True
        except ValueError:
            print(f"Choix invalide : {choice}. Ignoré.")
            invalid_choices = True

    if invalid_choices:
        return select_characters(character_type)
    else:
        print(chosen_characters)
        return chosen_characters

selected_tank_characters = select_characters("Tank")
selected_attacker_characters = select_characters("Attacker")