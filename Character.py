from __future__ import annotations
from Dice import Dice, RiggedDice
from rich.console import Console

class Character:
    _max_health = 20
    _current_health = _max_health
    _attack_value = 5
    _defense_value = 3
    _bleed_damage = 0  
    _rage_level = 0
    _life_steal = 0
    console = Console()

    
    def __init__(self, name: str, dice) -> None:
        self._name = name
        self._dice = dice
        
    def __str__(self):
        return f"I'm {self._name} the Character with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def get_name(self):
        return self._name
        
    def get_defense_value(self):
        return self._defense_value
    
    def is_alive(self):
        # return bool(self._current_health)
        return self._current_health > 0
        
    def regenerate(self):
        self._current_health = self._max_health
        
    def decrease_health(self, amount):
        amount = max(0, amount) 
        self._current_health = self._current_health - amount if self._current_health - amount >= 0 else 0
        self.show_healthbar()
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{"❤️" * self._current_health}{"🖤" * missing_hp}] {self._current_health}/{self._max_health}hp"
        # if self._max_health > 20:
        #     self._max_health = 20
        # elif self._current_health > self._max_health:
        #     self._current_health = self._max_health
        self.console.print(healthbar)

    def compute_damages(self, roll, target):
        return self._attack_value + roll

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        self.console.print(f"⚔️  {self._name} attack {target.get_name()} with {damages} damages in your face ! (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self, roll)
    
    def compute_wounds(self, damages, roll, attacker):
        if damages - self._defense_value - roll <= 0 or damages == 0:
            return 0
        else:
            print(f"computed :{damages - self._defense_value - roll}")
            return damages - self._defense_value - roll
    
    def defense(self, damages, attacker, roll):
        roll = self._dice.roll()
        wounds = 0 if damages == 0 else self.compute_wounds(damages, roll, attacker) 
        self.console.print(f"🛡️  {self._name} take {wounds} wounds from {attacker.get_name()} in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        print(f"decrease {wounds}")
        self.decrease_health(wounds)

    def apply_defense_reduction(self, reduction):
        self.console.print(f"🔒  {self._name}'s defense reduced by {reduction}.")
        self._defense_value -= reduction

          
