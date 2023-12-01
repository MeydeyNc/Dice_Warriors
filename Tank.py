from random import randint

from Character import Character


class Paladin(Character):

    _max_health = Character._max_health + randint(10,25)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(5,12)
    _defense_value = Character._defense_value + randint(5,15)


    def __str__(self):
        return super().__str__()
    
    def decrease_health(self, amount):
        if (amount >= 0):
            rollD4 = randint(1,4)
            if rollD4 == 1:
                if amount <= 0 :
                    amount = 0
                else: 
                    self.console.print(f" 🟩 Bonus : 🧝 The {self._name} Holy Armor reduces wounds by 3")
                    amount -= 3
            elif rollD4 == 2:
                randomAttack = randint(-3,5)
                self._attack_value = self._attack_value + randomAttack
                self.console.print(f" 🟩 Bonus : 🧝 The {self._name} calls to the Holy light to gain attack ✨ , attack + {self._attack_value} (roll : {randomAttack})")
            elif rollD4 == 3:
                randomDefense = randint(-1,7)
                self._defense_value = self._defense_value + randomDefense
                self.console.print(f" 🟩 Bonus : 🧝 The {self._name} calls to his faith to gain defense ⛨ , defense + {self._defense_value} (roll : {randomDefense})")
            else:
                randomFaith = randint(-1,10)
                if (self._current_health + randomFaith >= self._max_health):
                        self._current_health = self._max_health
                else:
                    self._current_health += randomFaith  
                    self.console.print(f" 🟩 Bonus : 🧝 The {self._name} heals himself thanks to his faith ✨, HP + {self._current_health} (roll : {randomFaith})")
                    
        return super().decrease_health(amount)


class Phantom_Warden(Character):

    _max_health = Character._max_health + randint(5,9)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(3,8)
    _defense_value = Character._defense_value + randint(10,15)


    def __str__(self):
        return super().__str__()
    
    def compute_wounds(self, damages, roll, attacker):
       roll: int = self._dice.roll()
       if (roll == self._dice._faces):
           self.console.print(f" 🟩 Bonus : 👻 The {self._name} evaporated throught the attack 🌫️ ! (Wounds : 0)")
           return super().compute_wounds(0, 0, attacker)   
       elif (roll == 1):
           self.console.print(f" 🟥 Malus : 👻 The {self._name} missed is escape ... 💫 (Wounds x 2)")
           return super().compute_wounds(damages*2, roll, attacker)

       else:
           self.console.print(f" 🟩 Bonus : 👻 The {self._name} evaded the attack 💨 ! (Wounds - {roll})")
           if round(super().compute_wounds(damages, roll, attacker) - roll) <= 0:
                return 0
           else:
               return round(super().compute_wounds(damages, roll, attacker) - roll)


class Leviathan(Character):

    _max_health = Character._max_health + randint(8,12)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(5,7)
    _defense_value = Character._defense_value + randint(10,15)


    def __str__(self):
        return super().__str__()
    
    def decrease_health(self, amount):
        if (self._current_health < self._max_health):
           coinThrow = randint(1,2)
           if coinThrow == 1:
               self.console.print(f"🟥 Malus : 🐙 The {self._name} failed to restore health points")            
           else : 
               restore_roll = randint(1,10)
               if (restore_roll == 10):
                    self.console.print(f" 🟩 Bonus : 🐙 The {self._name} restored 4 health points ✨")
                    if (self._current_health + restore_roll > self._max_health):
                        self._current_health = self._max_health
                    else:
                        self._current_health += 10  
               elif (restore_roll == 1):
                  self.console.print(f" 🟥 Malus : 🐙 The {self._name} didn't succeed to restore health points")
                  
               else:
                    self.console.print(f" 🟩 Bonus : 🐙 The {self._name} restored {restore_roll} HP ✨")
                    if (self._current_health + restore_roll > self._max_health):
                        self._current_health = self._max_health
                    else:
                        self._current_health += restore_roll
                        
        super().decrease_health(amount)
        

class Guardian(Character):

    _max_health = Character._max_health + randint(5,9)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(3,8)
    _defense_value = Character._defense_value + randint(5,15)    


    def __str__(self):
        return super().__str__()
    
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0:
            amount = self._current_health
            super().decrease_health(amount) 
        else:
            rollD4 = randint(1,4)
            if not rollD4 == 4:
                self.console.print(f" 🟥 Malus : ♖ The {self._name} failed to gain defense as he's weakened by the Attacker 💔")
                super().decrease_health(amount) 
            else:
                if self._current_health - amount > 0 and amount -1 > 0:
                    self._defense_value += 2
                    self.console.print(f" 🟩 Bonus : ♖ The {self._name} enrages 💢 and gain 2 defense points !")
                super().decrease_health(amount) 

                   
class Shield_Master(Character):

    _max_health = Character._max_health + randint(2,5)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(3,8)
    _defense_value = Character._defense_value + randint(7,15)  


    def __str__(self):
        return super().__str__()
    
    def compute_wounds(self, damages, roll, attacker: Character):
        rollD6 = randint(1,6)
        if rollD6 == 1:
            self.console.print(f" 🟥 Malus : 🛡️ The {self._name} didn't succeeded in his parry")
            return super().compute_wounds(damages, roll, attacker)
        elif rollD6 == 6:
            self.console.print(f" 🟩 Bonus : 🛡️ The {self._name} parried your attack for a Critical Hit 💢 ! (Sends back {damages})")
            attacker.decrease_health(damages) 
            return 0
        else:
            self.console.print(f" 🟩 Bonus : 🛡️ The {self._name} parried your attack 💫 ! ({damages}/{rollD6} ≈ {round(damages/rollD6)})")
            return super().compute_wounds(round(damages/rollD6), roll, attacker)


if __name__ == "__main__":
    exec(open("main.py").read())
