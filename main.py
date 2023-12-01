from __future__ import annotations
import importlib
from random import choice
import time

from Team import Team
from Fight import attack_team, check_for_win
from Conf import set_conf


if __name__ == "__main__":
    
    red_team = Team(is_red_team=True)
    blue_team = Team(is_red_team=False)
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
