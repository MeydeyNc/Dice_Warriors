from __future__ import annotations
from random import randint
from rich.console import Console


# Do not remove blanck ! 

class Character:
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(7, 13)
    _defense_value = randint(2, 5)
    
    console = Console()
    
    def __init__(self, name: str, dice) -> None:
        self._name = name
        self._dice = dice
        
    def __str__(self):
        return f"I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF]"
    
    def printInfo(self):
        self.console.print(f"I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF]")
    
    def get_name(self):
        return self._name
    
    def get_current_health(self):
        return self._current_health
        
    def get_attack_value(self):
        return self._attack_value
    
    def get_defense_value(self):
        return self._defense_value
    
    def is_alive(self):
        return self._current_health > 0
        
    def regenerate(self):
        self._current_health = self._max_health
        
    def decrease_health(self, amount):
        amount = max(0, amount) 
        self._current_health = self._current_health - amount if self._current_health - amount >= 0 else 0
        self.show_healthbar()
        if not self.is_alive():
            return
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        if self._current_health < self._max_health and self._current_health > 0:
            healthbar = f" {self._name} [{"[#E1E120]◼[/#E1E120]" * self._current_health}{"[#E11818]◼[/#E11818]" * missing_hp}] [#E1E120]{self._current_health}[/#E1E120]/[#6D9C2B]{self._max_health}[/#6D9C2B] [#E1E120]HP[/#E1E120]"
        elif self._current_health == 0:
            healthbar = f" {self._name} [{"[#E11818]◼[/#E11818]" * self._current_health}{"[#E11818]◼[/#E11818]" * missing_hp}] [#E11818]{self._current_health}[/#E11818]/[#E11818]{self._max_health}[/#E11818] [#E11818]HP[/#E11818]"
        else:
            healthbar = f" {self._name} [{"[#6D9C2B]◼[/#6D9C2B]" * self._current_health}{"[#6D9C2B]◼[/#6D9C2B]" * missing_hp}] [#6D9C2B]{self._current_health}[/#6D9C2B]/[#6D9C2B]{self._max_health}[/#6D9C2B] [#6D9C2B]HP[/#6D9C2B]"

        self.console.print(healthbar)
        self.console.rule(f"{self._name}", style='bold blue3' if 'blue' not in self._name else f'bold red3')
        
    def compute_damages(self, roll, target):
        return self._attack_value + roll

    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        self.console.print(f" ⚔️    {self._name} [#E01631]attack[/#E01631] {target.get_name()} with [#ff0000]{damages}[/#ff0000] [#ff0000]damages[/#ff0000] in your face ! ([#E01631]Attack[/#E01631]: [#E01631]{self._attack_value}[/#E01631] + 🎲 [#0095bd]roll[/#0095bd]: [#0095bd]{roll}[/#0095bd])")
        target.defense(damages, self)
    
    def compute_wounds(self, damages, roll, attacker):
        if damages - self._defense_value - roll <= 0 or damages == 0:
            return 0
        else:
            return damages - self._defense_value - roll
    
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        wounds = 0 if damages == 0 else self.compute_wounds(damages, roll, attacker) 

        self.console.print(f" 🛡️    {self._name} take [#ff0000]{wounds}[/#ff0000] [#ff0000]wounds[/#ff0000] from {attacker.get_name()} ! ([#ff0000]damages[/#ff0000]: [#E01631]{damages}[/#E01631] - [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] - 🎲 [#0095bd]roll[/#0095bd]: [#0095bd]{roll}[/#0095bd])")
        self.decrease_health(wounds)

    def apply_defense_reduction(self, reduction):
        self.console.print(f" 🔒    {self._name}'s [#6D05FF]defense[/#6D05FF] reduced by {reduction}.")
        self._defense_value -= reduction


if __name__ == "__main__":
    exec(open("main.py").read())
