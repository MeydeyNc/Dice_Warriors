from __future__ import annotations
from random import choice
from rich.console import Console

def attack_team(attacker, target_team):
    target_tanks = [tank for tank in target_team.tanks if tank.is_alive()]
    if target_tanks:
        target_tank = choice(target_tanks)
        attacker.attack(target_tank)
    else:
        target_attackers = [attacker for attacker in target_team.attackers if attacker.is_alive()]
        if target_attackers:
            target_attacker = choice(target_attackers)
            attacker.attack(target_attacker)

def print_team_result(team, team_name):
    console = Console()
    console.print(f"[bold {team_name}] {team_name} Team wins! [/bold {team_name}]")
    for char in team.attackers + team.tanks:
        if char.is_alive():
            chara = char.__str__()
            console.print(chara)
            char.show_healthbar()
    for char in team.attackers + team.tanks:
        if not char.is_alive():
            chara = char.__str__()
            console.print(chara)
            char.show_healthbar()

def check_for_win(red_team, blue_team):
    if not any(char.is_alive() for char in blue_team.attackers + blue_team.tanks):
        print_team_result(red_team, 'Red')
        return True
    elif not any(char.is_alive() for char in red_team.attackers + red_team.tanks):
        print_team_result(blue_team, 'Blue')
        return True
    return False
