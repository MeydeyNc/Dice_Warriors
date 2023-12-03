from __future__ import annotations
from random import randint

from Character import Character


class Warrior(Character):

    _max_health = Character._max_health + randint(2, 4)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(5, 15)
    _defense_value = Character._defense_value + randint(3, 5)
    _attack_bonus = randint(2, 5)
    
    def __str__(self):
        return f" ⚔️  I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF] ⚔️" 
    
    def compute_damages(self, roll, target):
        damages = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : ⚔️  The {self._name}'s sword slashed severely {target.get_name()} with [#FFA500]{self._attack_bonus}[/#FFA500] [#E01631]attack[/#E01631] bonus 💢")
            damages += self._attack_bonus
            self._attack_bonus += self._attack_bonus
        elif roll == 1:
            self.console.print(f" 🟥 Malus : ⚔️  The {self._name} failed to [#E01631]attack[/#E01631]  ( 🎲 [#0095bd]rolled[/#0095bd] : [#0095bd]{roll}[/#0095bd]) ! The {self._name}'s sword comes back straight to his face 😵 The {self._name} takes [#ff0000]{min(self._current_health -1, self._attack_bonus)}[/#ff0000] [#ff0000]damages[/#ff0000].")
            self.decrease_health(min(self._current_health -1, self._attack_bonus))
            damages = 0

        return damages


class Thief(Character):  

    _max_health = Character._max_health + randint(2, 4)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(15, 25)
    _defense_value = Character._defense_value + randint(1, 3)
    _life_steal = randint(2, 5)
    
    def __str__(self):
        return f" 🗡️  I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF]  🗡️"

    def compute_damages(self, roll, target: Character):
        self.console.print(f" 🟩 Bonus : 🗡️  {self._name}'s sneaky [#E01631]attack[/#E01631] 🗡️  ignored the {target.get_name()}'s [#6D05FF]defense[/#6D05FF] : [#6D05FF]{target.get_defense_value()}[/#6D05FF])")
        damages = super().compute_damages(roll, target) + target.get_defense_value()

        if roll == self._dice._faces: 
            if self._current_health < self._max_health:
                self._current_health = min(self._current_health + self._life_steal, self._max_health)
                self.console.print(f" 🟩 Bonus : 🗡️  The {self._name} Additional [#ff0000]damages[/#ff0000] ! {self._name} performs Life steal 👤 gaining {self._life_steal} [#30CB00]HP[/#30CB00]")
                self.show_healthbar()
                return damages
        elif roll == 1:
            self._life_steal = max(0, self._life_steal - 2)
            self.console.print(f" 🟥 Malus : 🗡️  The {self._name} FAILED to steal [#30CB00]HP[/#30CB00] from the {target.get_name()} ([#0095bd]rolled[/#0095bd] : 🎲 [#0095bd]{roll}[/#0095bd]) ! {self._name}'s life steal reduced by {2}.")
            return damages
             
        return damages


class Berserker(Character):

    _max_health = Character._max_health + randint(2, 4)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(15, 25)
    _defense_value = Character._defense_value + randint(2, 4) 
    _rage_boost = 0
    
    def __str__(self):
        return f" 🐻 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF] 🐻"
    
    def compute_damages(self, roll, target: Character):
        self._rage_boost += 2
        damages = super().compute_damages(roll, target)
        if self._current_health < self._max_health:
            
            self.console.print(f" 🟩 Bonus : 🐻 The {self._name} enrages ! [#E01631]attack[/#E01631] bonus: [#ff0000]{self._rage_boost*2}[/#ff0000]")
            return damages + self._rage_boost*2
        
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 🐻 The {self._name} got additional [#ff0000]damages[/#ff0000] ! [#E01631]attack[/#E01631] bonus: [#ff0000]{max(2,self._rage_boost)}[/#ff0000]")
            return damages + max(2,self._rage_boost)
        
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 🐻 The {self._name} failed to gain rage (: {roll}) ! [#E01631]attack[/#E01631] reduced by [#ff0000]{max(2,self._rage_boost)}[/#ff0000]")
            return damages - max(2,self._rage_boost)
        return damages


class Samurai(Character):

    _max_health = Character._max_health + randint(2, 4)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(15, 25)
    _defense_value = Character._defense_value + randint(2, 6)
    _bleed_damage = randint(2, 4)  
    
    def __str__(self):
        return f" 👺 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF] 👺"
    
    def compute_damages(self, roll, target: Character):
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 👺 The {self._name} inflicted a deep wound making {target.get_name()} bleed for additional [#ff0000]{self._bleed_damage}[/#ff0000] overturns [#ff0000]damages[/#ff0000] ([#0095bd]rolled[/#0095bd] = 🎲 [#0095bd]{roll}[/#0095bd])")
            damage += self._bleed_damage
            self._bleed_damage += self._bleed_damage
            return damage
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 👺 The {self._name} failed to [#E01631]attack[/#E01631] ! The {self._name} inflicts [#ff0000]self-damage[/#ff0000], loosing [#ff0000]{min(self._current_health -1, self._bleed_damage)}[/#ff0000] [#30CB00]HP[/#30CB00]")
            self.decrease_health(min(self._current_health -1, self._bleed_damage))
            return 0
        return damage


class Mage(Character):

    _max_health = Character._max_health + randint(2, 4)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(15, 25)
    _defense_value = Character._defense_value + randint(1, 2)
    _target_defense_reduction = randint(4, 6)
    
    def __str__(self):
        return f" 🧙 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#00A5FF]{self._defense_value}[/#00A5FF] 🧙"
    
    def compute_damages(self, roll, target: Character):
        self.console.print(f" 🌌🧙 {self._name} casts 🔥 [#f4ac00]Fireball[/#f4ac00] 🔥 !")
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 🧙 The {self._name}'s [#f4ac00]Fireball[/#f4ac00] inflicts burn 🔥 ! The armor of {self._target_defense_reduction} is [#ffff00]melting[/#ffff00] !")
            if target.get_defense_value() >= self._target_defense_reduction :
               target.apply_defense_reduction(self._target_defense_reduction)
               return damage
            else :
                boost = self._target_defense_reduction - target.get_defense_value()
                target.apply_defense_reduction(boost)
                return damage + boost
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 🧙 The {self._name} FAILED to cast ! {self._name}'s [#f4ac00]Fireball[/#f4ac00] 🔥 backfires 💥 , inflicting [#ff0000]self-damages[/#ff0000].")
            self.decrease_health(min(self._current_health -1, self._target_defense_reduction))
            return damage
        
        return damage


if __name__ == "__main__":
    exec(open("main.py").read())
