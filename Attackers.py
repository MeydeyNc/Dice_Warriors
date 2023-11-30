from random import randint

from Character import Character


class Warrior(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _attack_bonus = randint(2, 5)
    
    def __str__(self):
        return super().__str__()
    
    def compute_damages(self, roll, target):
        damages = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : ⚔️ The {self._name}'s sword slashed severely {target._name} with {self._attack_bonus} attack bonus 💢")
            damages += self._attack_bonus
            self._attack_bonus += self._attack_bonus
        elif roll == 1:
            self.console.print(f" 🟥 Malus : ⚔️ The {self._name} failed to attack  (rolled : {roll}) ! The {self._name}'s sword comes back straight to his face 😵 The {self._name} takes {self._attack_bonus} damages.")
            self.decrease_health(self._attack_bonus)
            damages = 0

        return damages


class Thief(Character):  
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _life_steal = randint(2, 5)
    
    def __str__(self):
        return super().__str__()

    def compute_damages(self, roll, target: Character):
        self.console.print(f" 🟩 Bonus: 🗡️ {self._name}'s sneaky attack 🗡️ ignored the {target._name}'s defense : {target.get_defense_value()})")
        damages = super().compute_damages(roll, target) + target.get_defense_value()

        if roll == self._dice._faces: 
            if self._current_health < self._max_health:
                self._current_health = min(self._current_health + self._life_steal, self._max_health)
                self.console.print(f" 🟩 Bonus : 🗡️ The {self._name} Additional damages ! {self._name} performs Life steal 👤 gaining {self._life_steal} HP")
                self.show_healthbar()
                return damages
        elif roll == 1:
            self._life_steal = max(0, self._life_steal - 2)
            self.console.print(f" 🟥 Malus : 🗡️ The {self._name} FAILED to steal HP from the {target._name} (rolled : {roll}) ! {self._name}'s life steal reduced by {2}.")
            return damages
             
        return damages


class Berserker(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7) 
    _rage_boost = 0
    
    def __str__(self):
        return super().__str__()
    
    def compute_damages(self, roll, target: Character):
        self._rage_boost += 2
        damages = super().compute_damages(roll, target)
        if self._current_health < self._max_health:
            
            self.console.print(f" 🟩 Bonus : 🐻 The {self._name} enrages ! Attack bonus: {self._rage_boost*2}")
            return damages + self._rage_boost*2
        
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 🐻 The {self._name} got additional damages ! Attack bonus: {max(2,self._rage_boost)}")
            return damages + max(2,self._rage_boost)
        
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 🐻 The {self._name} failed to gain rage (: {roll}) ! Attack reduced by {max(2,self._rage_boost)}")
            return damages - max(2,self._rage_boost)
        return damages


class Samurai(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    _bleed_damage = randint(2, 4)  
    
    def __str__(self):
        return super().__str__()
    
    def compute_damages(self, roll, target: Character):
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 👺 The {self._name} inflicted a deep wound making {target._name} bleed for additional {self._bleed_damage} overturns damages (rolled = {roll})")
            damage += self._bleed_damage
            self._bleed_damage += self._bleed_damage
            return damage
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 👺 The {self._name} failed to attack ! The {self._name} inflicts self-damage, loosing {self._bleed_damage if self._bleed_damage <= self._current_health - self._bleed_damage else self._current_health} HP")
            self.decrease_health(self._bleed_damage)
            return 0
        return damage


class Mage(Character):
    _max_health = randint(18, 22)
    _current_health = _max_health
    _attack_value = randint(25, 40)
    _defense_value = randint(4, 7)
    target_defense_reduction = randint(4, 6)
    
    def __str__(self):
        return super().__str__()
    
    def compute_damages(self, roll, target: Character):
        self.console.print(f" 🌌🧙 {self._name} casts Fireball 🔥 !")
        damage = super().compute_damages(roll, target)
        if roll == self._dice._faces:
            self.console.print(f" 🟩 Bonus : 🧙 The {self._name}'s Fireball inflicts burn 🔥 ! The armor of {self.target_defense_reduction} is melting !")
            if target._defense_value >= self.target_defense_reduction :
               target.apply_defense_reduction(self.target_defense_reduction)
               return damage
            else :
                boost = self.target_defense_reduction - target._defense_value
                target._defense_value = 0
                return damage + boost
        elif roll == 1:
            self.console.print(f" 🟥 Malus : 🧙 The {self._name} FAILED to cast ! {self._name}'s Fireball 🔥 backfires 💥 , inflicting self-damages.")
            self.decrease_health(self.target_defense_reduction)
            return damage
        
        return damage


if __name__ == "__main__":
    exec(open("main.py").read())
