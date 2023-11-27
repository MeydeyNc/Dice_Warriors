from random import randint
from Dice import *
from Character import *


class Warrior(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    _attack_bonus = randint(2, 5)
    def compute_damages(self, roll, target):
        damages = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            print(f"🪓 Bonus: Axe in your face ({self._attack_bonus} attack)")
            damages += self._attack_bonus
            self._attack_bonus += self._attack_bonus
        elif roll == 1:
            print(f"🩸 The roll result is {roll}. You FAILED ! The axe comes back straight to the face. {self._name} takes {self._attack_bonus} damages.")
            self.decrease_health(self._attack_bonus)
            damages = 0
        else:
            print(f"🎲 The roll result is {roll}. No additional damage or life steal this time!")

        return damages
    
class Thief(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    _life_steal = randint(2, 5)
    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneacky attack (ignore defense: + {target.get_defense_value()} bonus)")
        damages = super().compute_damages(roll, target) + target.get_defense_value()

        if roll == self._dice._faces:
            if self._current_health < self._max_health:
                life_stolen = min(self._life_steal, self._max_health - self._current_health)
                self._current_health += life_stolen
                # self._current_health = min(self._current_health, self._max_health)
                self._life_steal += self._life_steal
                print(f"👤  Additional damage! Thief performs Life steal, gaining {life_stolen} life.")
            else:
                pass
            # ??
        elif roll == 1: # ça retire 2 avant d'afficher donc on le voit pas mais ça fonctionne.
            self._life_steal -= 2
            self._life_steal = max(0, self._life_steal)
            print(f"🩸 The roll result is {roll}. You FAILED! Thief's life steal reduced by {2}.")
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
            print(f"Additional damage! Attack bonus: {max(2,self._rage_level)}")
            damages += max(2,self._rage_level)
        elif roll == 1:
            print(f"🩸  The roll result is {roll}. You FAILED! Attack reduced by {max(2,self._rage_level)}.")
            damages -= max(2,self._rage_level)
        else:
            print(f"🎲 The roll result is {roll}. No additional damage this time!")
        return damages

 
class Samurai(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(10, 15)
    _defense_value = randint(4, 7)
    _bleed_damage = randint(2, 4)  
    def compute_damages(self, roll, target: Character):
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            print(f"💉 Bleeding attack! Inflicting additional damage over time. Roll = {roll}. Bonus {self._bleed_damage} attack")
            damage += self._bleed_damage
            self._bleed_damage += self._bleed_damage
        elif roll == 1:
            print(f"🩸 The roll result is {roll}. You FAILED! Samurai inflicts self-damage, losing {self._bleed_damage} HP.")
            self.decrease_health(self._bleed_damage)
            damage = 0
        else:
            print(f"🎲 The roll result is {roll}. No additional damages this time!")
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
            target_defense_reduction = 6
            target.apply_defense_reduction(target_defense_reduction, self.burn_duration)
        elif roll == 1:
            self._current_health -= 2
            print(f"🩸 The roll result is {roll}. You FAILED! Mage's Fireball backfires, inflicting self-damage.")
        else:
            print(f"🎲 The roll result is {roll}. The Fireball does not inflict Burn!")
        return damage

