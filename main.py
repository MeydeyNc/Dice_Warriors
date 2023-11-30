from __future__ import annotations
from random import randint, choice, shuffle
from rich.console import Console
from rich import print
from Attackers import Samurai, Berserker, Mage, Thief, Warrior
from Tank import Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian
from Dice import Dice


class Team:
    _game_dice = 6
    _max_instances = 1 # of each class
    _team_len = 5 # by type_class (= class file name) (1 to 5*_max_instances)
    
    def __init__(self, is_red_team: bool):
        self.is_red_team = is_red_team
        self.tanks = self._create_team([Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian], self._max_instances)
        self.attackers = self._create_team([Samurai, Berserker, Mage, Thief, Warrior], self._max_instances)
    def _create_team(self, character_classes, max_instances):
        character_instances = []

        for character_class in character_classes:
            instances = [character_class(f"{character_class.__name__} n°{i+1} {'[bold blue]BLUE Team[/bold blue]' if not self.is_red_team else '[bold red]RED Team[/bold red]'}", Dice(self._game_dice)) for i in range(max_instances)]
            character_instances.extend(instances)

        shuffle(character_instances)
        return character_instances[:self._team_len]

if __name__ == "__main__":
    red_team = Team(is_red_team=True)
    blue_team = Team(is_red_team=False)

    red_attacker_turn = choice([True, False])
    
    # log every fighters (first team of attackers chosed)
    
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
                console = Console()
                console.print("[bold red]Red Team wins![/bold red]")
                for char in red_team.attackers + red_team.tanks:
                    if char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
                        char.show_healthbar()
                for char in red_team.attackers + red_team.tanks:
                    if not char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
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
                console = Console()
                console.print("[bold blue]Blue Team wins![/bold blue]")
                for char in blue_team.attackers + blue_team.tanks:
                    if char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
                        char.show_healthbar()
                for char in blue_team.attackers + blue_team.tanks:
                    if not char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
                        char.show_healthbar()
                break
        if not any(char.is_alive() for char in blue_team.attackers + blue_team.tanks):
                console = Console()
                console.print("[bold red]Red Team wins![/bold red]")
                for char in red_team.attackers + red_team.tanks:
                    if char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
                        char.show_healthbar()
                for char in red_team.attackers + red_team.tanks:
                    if not char.is_alive():
                        chara = char.__str__()
                        console.print(chara)
                        char.show_healthbar()
                break
        red_attacker_turn = not red_attacker_turn