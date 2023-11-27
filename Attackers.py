from random import randint
from Dice import *
from Character import *


class Warrior(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    def compute_damages(self, roll, target):
        damages = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            print("🪓 Bonus: Axe in your face (+3 attack)")
            damages += 3
        elif roll == 1:
            self._current_health -= 3
            print(f"🩸 The roll result is {roll}. You FAILED ! The axe comes back straight to the face. {self._name} takes 3 damage.")
            damages = 0
        else:
            print(f"🎲 The roll result is {roll}. No additional damage or life steal this time!")

        return damages
    
class Thief(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    _life_steal = 3
    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneacky attack (ignore defense: + {target.get_defense_value()} bonus)")
        damages = super().compute_damages(roll, target) + target.get_defense_value()

        if roll == self._dice._faces and self._current_health < self._max_health:
            life_stolen = min(self._life_steal, self._max_health - self._current_health)
            self._current_health += life_stolen
            print(f"👤  Additional damage! Thief performs Life steal, gaining {life_stolen} life.")
        elif roll == 1: # ça retire 2 avant d'afficher donc on le voit pas mais ça fonctionne.
            self._attack_value -= 2
            print(f"🩸 The roll result is {roll}. You FAILED! Thief's attack reduced by 2.")
        else:
            print(f"🎲 The roll result is {roll}. No additional damage or life steal this time!")

        return damages


class Berserker(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7) 
    _rage_level = -1
    def compute_damages(self, roll, target: Character):
        self._rage_level += 1
        damages = super().compute_damages(roll, target)
        if self._current_health < self._max_health:
            print(f"🎭 Berserker enters rage level {self._rage_level}! Attack bonus: +{self._rage_level}")
            damages += self._rage_level
        if roll == self._dice._faces:
            print(f"Additional damage! Attack bonus: +2")
            damages += 2
        elif roll == 1:
            print(f"🩸  The roll result is {roll}. You FAILED! Attack reduced by 2.")
            damages -= 2
        else:
            print(f"🎲 The roll result is {roll}. No additional damage this time!")
        return damages

 
class Samurai(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    _bleed_damage = 2  
    def compute_damages(self, roll, target: Character):
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            print(f"💉 Bleeding attack! Inflicting additional damage over time. Roll = {roll}. Bonus +2 attack")
            damage += self._bleed_damage
        elif roll == 1:
            self._current_health -= 2 
            print(f"🩸 The roll result is {roll}. You FAILED! Samurai inflicts self-damage, losing 2 health.")
            damage = 0
        else:
            print(f"🎲 The roll result is {roll}. No additional damage this time!")
        return damage


class Mage(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    def compute_damages(self, roll, target: Character):
        print("🔥 Mage casts Fireball !")
        self.burn_duration = 3 
        damage = super().compute_damages(roll, target)
        if roll < self._dice._faces:
            print(f"🔥 {self._name}'s Fireball inflicts Burn! Defense reduction for {self.burn_duration} turns.")
            target_defense_reduction = 2 
            target.apply_defense_reduction(target_defense_reduction, self.burn_duration)
        elif roll == 1:
            self._current_health -= 2
            print(f"🩸 The roll result is {roll}. You FAILED! Mage's Fireball backfires, inflicting self-damage.")
        else:
            print(f"🎲 The roll result is {roll}. The Fireball does not inflict Burn!")
        return damage

