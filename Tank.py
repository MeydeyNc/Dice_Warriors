from random import randint

from Character import Character
from Dice import Dice

class Paladin(Character):
    _max_health = Character._max_health + randint(10,25)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(5,12)
    _defense_value = Character._defense_value + randint(5,15)

    def __str__(self):
        return f" 🧝 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] 🧝"
    
    def decrease_health(self, amount):
        if (amount >= 0):
            rollD4 = Dice(4).roll()
            if rollD4 == 1:
                if amount <= 0 :
                    amount = 0
                else: 
                    self.console.print(f" 🟩 Bonus : 🧝 The {self._name} Holy Armor reduces [#ff0000]wounds[/#ff0000] by 3")
                    amount -= 3
            elif rollD4 == 2:
                randomAttack = randint(-3,5)
                self._attack_value = self._attack_value + randomAttack
                self.console.print(f" 🟩 Bonus : 🧝 The {self._name} calls to the Holy light to gain [#E01631]attack[/#E01631] ✨ ! [#E01631]attack[/#E01631] + [#E01631]{self._attack_value}[/#E01631] ( 🎲 [#0095BD]roll[/#0095BD] : [#E01631]{randomAttack}[/#E01631])")
            elif rollD4 == 3:
                randomDefense = randint(-1,7)
                self._defense_value = self._defense_value + randomDefense
                self.console.print(f" 🟩 Bonus : 🧝 The {self._name} calls to his faith to gain [#6D05FF]defense[/#6D05FF] ⛨ ! [#6D05FF]defense[/#6D05FF] + [#6d05ff]{self._defense_value}[#6d05ff] ( 🎲 [#0095BD]roll[/#0095BD] : [#6D05FF]{randomDefense}[/#6D05FF])")
            else:
                randomFaith = randint(-1,10)
                if (self._current_health + randomFaith >= self._max_health):
                        self._current_health = self._max_health
                else:
                    self._current_health += randomFaith  
                    self.console.print(f" 🟩 Bonus : 🧝 The {self._name} heals himself thanks to his faith ✨, [#30CB00]HP[/#30CB00] + [#E1E120]{self._current_health}[/#E1E120] ( 🎲 [#0095BD]roll[/#0095BD] : {randomFaith})")
                    
        return super().decrease_health(amount)


class Phantom_Warden(Character):

    _max_health = Character._max_health + randint(5,9)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(3,8)
    _defense_value = Character._defense_value + randint(10,15)


    def __str__(self):
        return f" 👻 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] 👻"
    
    def compute_wounds(self, damages, roll, attacker):
       roll: int = self._dice.roll()
       if (roll == self._dice._faces):
           self.console.print(f" 🟩 Bonus : 👻 The {self._name} evaporated throught the [#E01631]attack[/#E01631] 🌫️ ! ([#ff0000]Wounds[/#ff0000] : 0)")
           return super().compute_wounds(0, 0, attacker)   
       elif (roll == 1):
           self.console.print(f" 🟥 Malus : 👻 The {self._name} missed is escape ... 💫 ([#ff0000]wounds[/#ff0000] x 2)")
           return super().compute_wounds(damages*2, roll, attacker)

       else:
           self.console.print(f" 🟩 Bonus : 👻 The {self._name} evaded the [#E01631]attack[/#E01631] 💨 ! ([#ff0000]wounds[/#ff0000] - 🎲 [#0095bd]{roll}[/#0095bd])")
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
        return f" 🐙 I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] 🐙"
    
    def decrease_health(self, amount):
        if (self._current_health < self._max_health):
           coinThrow = randint(1,2)
           if coinThrow == 1:
               self.console.print(f"🟥 Malus : 🐙 The {self._name} tried but failed to restore [#30CB00]HP[/#30CB00]")            
           else : 
               restore_roll = Dice(10).roll()
               if (restore_roll == 10):
                    self.console.print(f" 🟩 Bonus : 🐙 The {self._name} restored [#0095bd]{restore_roll}[/#0095bd] [#30CB00]HP[/#30CB00] ✨")
                    if (self._current_health + restore_roll > self._max_health):
                        self._current_health = self._max_health
                    else:
                        self._current_health += restore_roll  
               elif (restore_roll == 1):
                  self.console.print(f" 🟥 Malus : 🐙 The {self._name} didn't succeed to restore [#30CB00]HP[/#30CB00]")
                  
               else:
                    self.console.print(f" 🟩 Bonus : 🐙 The {self._name} restored [#0095bd]{restore_roll}[/#0095bd] [#30CB00]HP[/#30CB00] ✨")
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
        return f" ♖ I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] ♖"
    
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0:
            amount = self._current_health
            super().decrease_health(amount) 
        else:
            rollD4 = Dice(4).roll()
            if not rollD4 == 4:
                self.console.print(f" 🟥 Malus :  ♖ The {self._name} failed to gain [#6D05FF]defense[/#6D05FF] as he's weakened by the Attacker 💔")
                super().decrease_health(amount) 
            else:
                if self._current_health - amount > 0 and amount -1 > 0:
                    self._defense_value += 2
                    self.console.print(f" 🟩 Bonus : ♖ The {self._name} enrages 💢 and gain 2 [#6D05FF]defense[/#6D05FF] points !")
                super().decrease_health(amount) 

                   
class Shield_Master(Character):

    _max_health = Character._max_health + randint(2,5)
    _current_health = _max_health
    _attack_value = Character._attack_value + randint(3,8)
    _defense_value = Character._defense_value + randint(7,15)  


    def __str__(self):
        return f" 🛡️  I'm {self._name} with [#E01631]attack[/#E01631]: [#FFA500]{self._attack_value}[/#FFA500] and [#6D05FF]defense[/#6D05FF]: [#6d05ff]{self._defense_value}[/#6d05ff] 🛡️"
    
    def compute_wounds(self, damages, roll, attacker: Character):
        rollD6 = Dice(6).roll()
        if rollD6 == 1:
            self.console.print(f" 🟥 Malus : 🛡️ The {self._name} didn't succeeded in his parry")
            return super().compute_wounds(damages, roll, attacker)
        elif rollD6 == 6:
            self.console.print(f" 🟩 Bonus : 🛡️ The {self._name} parried your [#E01631]attack[/#E01631] for a Critical Hit 💢 ! (Sends back {min(attacker.get_current_health() -1, damages)})")
            attacker.decrease_health(min(attacker.get_current_health() -1, damages)) 
            return super().compute_wounds(0, roll, attacker)
        else:
            self.console.print(f" 🟩 Bonus : 🛡️ The {self._name} parried your [#E01631]attack[/#E01631] 💫 ! ([#ff0000]{damages}[/#ff0000]/[#0095bd]{rollD6}[/#0095bd] ≈ {round(damages/rollD6)})")
            return super().compute_wounds(round(damages/rollD6), roll, attacker)


if __name__ == "__main__":
    exec(open("main.py").read())
