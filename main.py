from __future__ import annotations
from random import randint, choice
from Attackers import Samurai, Berserker, Mage, Thief, Warrior
from Tank import Paladin, Leviathan, Guardian, Phantom_Warden, Shield_Master
from Dice import Dice

_game_dice = randint(4, 9)

class Team:
    def __init__(self, is_red_team: bool):
        self.is_red_team = is_red_team
        self.tanks = self._create_team([Paladin, Leviathan, Phantom_Warden, Shield_Master]) # Guardian
        self.attackers = self._create_team([Samurai, Berserker, Mage, Warrior]) # Thief

    def _create_team(self, character_classes):
        return [character_class(f"{character_class.__name__}_{i}", Dice(_game_dice)) for i, character_class in enumerate(character_classes)]

if __name__ == "__main__":
    red_team = Team(is_red_team=True)
    blue_team = Team(is_red_team=False)

    red_attacker_turn = choice([True, False])

while any(char.is_alive() for char in red_team.attackers + red_team.tanks) and any(char.is_alive() for char in blue_team.attackers + blue_team.tanks):
    if red_attacker_turn:
        for attacker in red_team.attackers:
            if attacker.is_alive():
                target_tanks = [tank for tank in blue_team.tanks if tank.is_alive()]
                if target_tanks:
                    target_tank = choice(target_tanks)
                    attacker.attack(target_tank)
                else:
                    target_attackers = [attacker for attacker in blue_team.attackers if attacker.is_alive()]
                    if target_attackers:
                        target_attacker = choice(target_attackers)
                        attacker.attack(target_attacker)

        if not any(char.is_alive() for char in blue_team.attackers + blue_team.tanks):
            print("Red Team wins!")
            for char in red_team.attackers:
                if char.is_alive():
                    print(char)
                    char.show_healthbar()
            for char in blue_team.attackers:
                if char.is_alive():
                    print(char)
                    char.show_healthbar()
            break

    else:
        for attacker in blue_team.attackers:
            if attacker.is_alive():
                target_tanks = [tank for tank in red_team.tanks if tank.is_alive()]
                if target_tanks:
                    target_tank = choice(target_tanks)
                    attacker.attack(target_tank)
                else:
                    target_attackers = [attacker for attacker in red_team.attackers if attacker.is_alive()]
                    if target_attackers:
                        target_attacker = choice(target_attackers)
                        attacker.attack(target_attacker)

        if not any(char.is_alive() for char in red_team.attackers + red_team.tanks):
            print("Blue Team wins!")
            for char in blue_team.attackers:
                if char.is_alive():
                    print(char)
                    char.show_healthbar()
            break  # Exit the loop

    red_attacker_turn = not red_attacker_turn
