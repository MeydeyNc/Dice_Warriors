from Character import *
from Character import Character
from dataclass import Buff
from random import randint

class Paladin(Character):
    # Roll à 1  
    _max_health = randint(30,45)
    _current_health = _max_health
    _attack_value = randint(4,8)
    _defense_value = randint(10,15)
    
    def decrease_health(self, amount):
        if (self._current_health < self._max_health):
            
        return super().decrease_health(amount)
    
    rollD4 = randint(1,4)
    if rollD4 == 1:
        def compute_wounds(self, damages, roll, attacker):
            print("🔨 Bonus: Holy armor (-3 Wounds)")
            if round(super().compute_wounds(damages, roll, attacker) - roll) <= 0:
                return 0
            else:
                return round(super().compute_wounds(damages, roll, attacker) - 3)
    elif rollD4 == 2:
        _attack_value = _attack_value + 3
    elif rollD4 == 3:
        _defense_value = _defense_value + 3
    else:
        if (_current_health > _max_health):
                _current_health = _max_health
        else:
            _current_health += 3   
class Leviathan(Character):
    _max_health = randint(25,35)
    _current_health = _max_health
    _attack_value = randint(3,8)
    _defense_value = randint(10,15)
    def compute_wounds(self, damages, roll, attacker):
       roll: int = self._dice.roll()
       if (roll == self._dice._faces):
           print("🐙 Bonus : The Leviathan slipt throught the attack ! (Wounds / 2)")
           return round(super().compute_wounds(damages, roll, attacker) / 2)   
       elif (roll == 1):
           print("🐙 Malus : The Leviathan missed is escape ... (Wounds x 2)")
           return round(super().compute_wounds(damages, roll, attacker) * 2)
       else:
           print(f"🐙 Bonus : The Leviathan evaded the attack ! (Wounds - {roll})")
           if round(super().compute_wounds(damages, roll, attacker) - roll) <= 0:
                return 0
           else:
               return round(super().compute_wounds(damages, roll, attacker) - roll)

class Enforcer(Character):
    _max_health = randint(25,35)
    _current_health = _max_health
    _attack_value = randint(3,8)
    _defense_value = randint(10,15)
    def decrease_health(self, amount):
       if (self._current_health < self._max_health):
           coinThrow = randint(1,2)
           if coinThrow == 1:
               print(" Malus : The Guardian failed to restore health points")
               super().decrease_health(amount)
               
           else : 
               restore_roll = randint(1,10)
               if (restore_roll == 10):
                    print(" Bonus : The Guardian restored 4 health points")
                #   Encadrer la valeur de la vie max
                    if (self._current_health + restore_roll > self._max_health):
                        self._current_health = self._max_health
                    else:
                        self._current_health += 10
                        self.show_healthbar()
                  
               elif (restore_roll == 1):
                  print(" Malus : The Guardian failed to restore health points")
                  super().decrease_health(amount)
                  
               else:
                    print(f" Bonus : The Guardian restored {restore_roll} health points")
                #   Encadrer la valeur de la vie max
                    if (self._current_health + restore_roll > self._max_health):
                        self._current_health = self._max_health
                    else:
                        self._current_health += restore_roll
                        self.show_healthbar()
        

class Guardian(Character): # Enforcer 
    _max_health = randint(25,35)
    _current_health = _max_health
    _attack_value = randint(3,8)
    _defense_value = randint(10,15)    
    def decrease_health(self, amount):
        if (self._current_health - amount) < 0:
            amount = self._current_health
        else:
            rollD4 = randint(1,4)
            if not rollD4 == 4:
                print("🛡️ The Enforcer failed to gain defense as he's weakened by the Attacker")
            else:
                print("🛡️ The Enforcer enrages and gain defense !")
                self._defense_value += 1
                self._current_health -= amount
                # if (self._defense_value > 100):
                #     self._defense_value = 100
            self.show_healthbar()
       
class Shield_Master(Character):
   pass
