from __future__ import annotations

from Dice import Dice, RiggedDice
from dataclass import Buff

class Character:
    
    _max_health = 20
    _current_health = _max_health
    _attack_value = 5
    _defense_value = 3
    buff = Buff()
    
    def __init__(self, name: str, max_health: int, attack: int, defense: int, dice) -> None:
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice
        
    def __str__(self):
        return f"I'm {self._name} the Character with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def get_name(self):
        return self._name
        
    def get_defense_value(self):
        return self._defense_value
    
    def is_alive(self):
        # return bool(self._current_health)
        return self._current_health > 0 & self._current_health <= self._max_health 
        
    def regenerate(self):
        self._current_health = self._max_health
        
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0:
            amount = self._current_health  
        elif self._max_health > 20:
            self._max_health = 20
        elif self._current_health > self._max_health:
            self._current_health = self._max_health
            
        self._current_health -= amount
        self.show_healthbar()
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{"❤️" * self._current_health}{"🖤" * missing_hp}] {self._current_health}/{self._max_health}hp"
        if self._max_health > 20:
            self._max_health = 20
        elif self._current_health > self._max_health:
            self._current_health = self._max_health
        print(healthbar)

    def compute_damages(self, roll, target: Character):
        return self._attack_value + roll

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages in your face ! (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)
    
    def compute_wounds(self, damages, roll, attacker: Character):
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        wounds = self.compute_wounds(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)
