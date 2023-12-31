from __future__ import annotations
from random import choice
from rich.console import Console
from Team import Team
from Fight import attack_team, check_for_win

def print_team(team):
    console = Console()
    for tank in team.tanks:
        tank.printInfo()
    print("\n")
    for attacker in team.attackers:
        attacker.printInfo()

if __name__ == "__main__":
    
    red_team = Team(is_red_team=True)
    blue_team = Team(is_red_team=False)
    red_attacker_turn = choice([True, False])
    
    print_team(red_team)
    print_team(blue_team)
    
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
