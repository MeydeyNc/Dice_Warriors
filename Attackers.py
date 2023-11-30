from random import randint
from Dice import *
from Character import *


class Warrior(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _attack_bonus = randint(2, 5)
    def compute_damages(self, roll, target):
        damages = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            print(f"🪓 Bonus: {self._name} Axe in your face ({self._attack_bonus} attack)")
            damages += self._attack_bonus
            self._attack_bonus += self._attack_bonus
        elif roll == 1:
            self.console.print(f"🩸 The roll result is {roll}. You FAILED ! The {self._name} axe comes back straight to the face. {self._name} takes {self._attack_bonus} damages.")
            self.decrease_health(self._attack_bonus)
            damages = 0
        else:
            self.console.print(f"🎲 The roll result is {roll}. No additional damage or life steal this time for {self._name} !")

        return damages

class Thief(Character):  
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _life_steal = randint(2, 5)

    def compute_damages(self, roll, target: Character):
        self.console.print(f"🔪 Bonus: {self._name} Sneaky attack (ignore defense: + {target.get_defense_value()} bonus)")
        damages = super().compute_damages(roll, target) + target.get_defense_value()

        if roll == self._dice._faces: 
            if self._current_health < self._max_health:
                self._current_health = min(self._current_health + self._life_steal, self._max_health)
                self.console.print(f"👤  Additional damage! {self._name} performs Life steal, gaining {self._life_steal} life.")
                self.show_healthbar()
                return damages
        elif roll == 1:
            self._life_steal = max(0, self._life_steal - 2)
            self.console.print(f"🩸 The roll result is {roll}. You FAILED! {self._name}'s life steal reduced by {2}.")
            return damages
        else:
            self.console.print(f"🎲 The roll result is {roll}. No additional damage or life steal this time for {self._name} !")
            
        return damages


class Berserker(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7) 
    _rage_boost = 0
    def compute_damages(self, roll, target: Character):
        self._rage_boost += 2
        damages = super().compute_damages(roll, target)
        if self._current_health < self._max_health:
            
            self.console.print(f"🎭 {self._name} is enraged ! Attack bonus: +{self._rage_boost*2}")
            return damages + self._rage_boost*2
        
        if roll == self._dice._faces:
            self.console.print(f" {self._name} got additional damage! Attack bonus: {max(2,self._rage_boost)}")
            return damages + max(2,self._rage_boost)
        elif roll == 1:
            self.console.print(f"🩸  The {self._name} roll result is {roll}. You FAILED! Attack reduced by {max(2,self._rage_boost)}.")
            return damages - max(2,self._rage_boost)
        else:
            self.console.print(f"🎲 The {self._name} roll result is {roll}. No additional damages !")
        return damages

 
class Samurai(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _bleed_damage = randint(2, 4)  
    def compute_damages(self, roll, target: Character):
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f"💉 Bleeding attack! {self._name} inflict additional damage over time. Roll = {roll}. Bonus {self._bleed_damage} attack")
            damage += self._bleed_damage
            self._bleed_damage += self._bleed_damage
            return damage
        elif roll == 1:
            print(f"🩸 The roll result is {roll}. You FAILED! {self._name} inflicts self-damage, losing {self._bleed_damage if self._bleed_damage <= self._current_health - self._bleed_damage else self._current_health} HP.")
            self.decrease_health(self._bleed_damage)
            return 0
        else:
            self.console.print(f"🎲 The roll result is {roll}. No additional damages for {self._name} this time!")
        return damage


class Mage(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    target_defense_reduction = randint(4, 6)
    def compute_damages(self, roll, target: Character):
        print("🔥 Mage casts Fireball !")
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f"🔥 {self._name}'s Fireball inflicts Burn! Defense reduction of {self.target_defense_reduction}.")
            if target._defense_value >= self.target_defense_reduction :
               target.apply_defense_reduction(self.target_defense_reduction)
               return damage
            else :
                boost = self.target_defense_reduction - target._defense_value
                target._defense_value = 0
                return damage + boost


        elif roll == 1:
            self.console.print(f"🩸 The roll result is {roll}. You FAILED! {self._name}'s Fireball backfires, inflicting self-damage.")
            self.decrease_health(self.target_defense_reduction)
            return damage
        else:
            self.console.print(f"🎲 The roll result is {roll}. The {self._name}'s Fireball does not inflict Burn!")
        return damage

