from __future__ import annotations
from random import randint,  shuffle

from Attackers import Samurai, Berserker, Mage, Thief, Warrior
from Tank import Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian
from Dice import Dice

class Team:
    _game_dice = randint(4,9)
    _max_instances = 1 # of each class
    _team_len = randint(1,5)* _max_instances # by type_class (= class file name) (1 to 5*_max_instances)  
    def __init__(self, is_red_team: bool):
        self.is_red_team = is_red_team
        self.tanks = self._create_team([Paladin, Leviathan, Phantom_Warden, Shield_Master, Guardian], self._max_instances)
        self.attackers = self._create_team([Samurai, Berserker, Mage, Thief, Warrior], self._max_instances)
    def _create_team(self, character_classes, max_instances):
        character_instances = []

        for character_class in character_classes:
            instances = [character_class(f"{f'[bold blue]{character_class.__name__}[/bold blue]' if not self.is_red_team else f'[bold red]{character_class.__name__}[/bold red]'}{f' n°{i+1}' if i+1 > 1 else  ''}", Dice(self._game_dice)) for i in range(max_instances)]
            character_instances.extend(instances)

        shuffle(character_instances)
        return character_instances[:self._team_len]
    
if __name__ == "__main__":
    exec(open("main.py").read())
