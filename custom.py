from __future__ import annotations
from random import choice
from rich import print

from Dice import Dice
from champ_select import select_characters
from advanced import ask_user
from Fight import attack_team, check_for_win, print_team


class Custom_Team:

    _game_dice = ask_user("Choose game dice :   ")
   
    def __init__(self, is_red_team: bool):
        self.is_red_team = is_red_team
        self.tanks = self._create_team(select_characters("tank"), 1)
        self.attackers = self._create_team(select_characters("attacker"), 1)
    
    def _create_team(self, character_classes, max_instances):
        character_instances = []

        for character_class in character_classes:
            instances = [character_class(f"{f'[bold dark_blue]{character_class.__name__}[/bold dark_blue]' if not self.is_red_team else f'[bold dark_red]{character_class.__name__}[/bold dark_red]'}{f' n°{i+1}' if i+1 > 1 else  ''}", Dice(self._game_dice)) for i in range(max_instances)]
            character_instances.extend(instances)

        return character_instances


if __name__ == "__main__":
    
    try:
        print("[bold red]RED SELECTION ! [/bold red]")
        red_team = Custom_Team(is_red_team=True)
        print_team(red_team)
        print("[bold blue]BLUE SELECTION ! [/bold blue]")
        blue_team = Custom_Team(is_red_team=False)
        red_attacker_turn = choice([True, False])
            
        while any(char.is_alive() for char in red_team.attackers + red_team.tanks) and any(
            char.is_alive() for char in blue_team.attackers + blue_team.tanks):
            if red_attacker_turn:
                for attacker in red_team.attackers:
                    if attacker.is_alive():
                        attack_team(attacker, blue_team)

                if check_for_win(red_team, blue_team):
                    break
            else:
                for attacker in blue_team.attackers:
                    if attacker.is_alive():
                        attack_team(attacker, red_team)

                if check_for_win(red_team, blue_team):
                    break

            red_attacker_turn = not red_attacker_turn
    except KeyboardInterrupt:
        print("Game stopped")