from Character import *
from Character import Character
from dataclass import Buff
from random import randint

class Paladin(Character):
#    buff: Buff = Buff(randint(10, 40), randint(1, 6), randint(5, 20))
   def compute_wounds(self, damages, roll, attacker):
       print("🔨 Bonus: Holy armor (-3 Wounds)")
       return round(super().compute_wounds(damages, roll, attacker) - 3)
   
class Leviathan(Character):
#    buff: Buff = Buff(randint(10, 40), randint(1, 6), randint(5, 20))
   def compute_wounds(self, damages, roll, attacker):
       roll: int = self._dice.roll()
       if (roll == 6):
           print("🐙 Bonus : The Leviathan slipt throught the attack ! (Wounds / 2)")
           return round(super().compute_wounds(damages, roll, attacker) / 2)   
       elif (roll == 1):
           print("🐙 Malus : The Leviathan missed is escape ... (Wounds x 2)")
           return round(super().compute_wounds(damages, roll, attacker) * 2)
       else:
           print(f"🐙 Bonus : The Leviathan evaded the attack ! (Wounds - {roll})")
           return round(super().compute_wounds(damages, roll, attacker) - roll)

class Guardian(Character):
    pass
    # def decrease_health(self, amount):
    #     if (self._current_health < self._max_health):
    #         roll = self._dice.roll(2) # On veut une pièce ou un dé 2 quoi
    #         if not roll == 1:
    #             return super().decrease_health(amount)
    #         else : 
    #             restore_roll = self._dice.roll(4) # On veut un dé 4
    #             if (restore_roll == 4):
    #                     print("🛡️ Bonus : The Guardian restored 4 health points")
    #                     self._current_health += 4
    #             elif (restore_roll == 1):
    #                     print("🛡️ Malus : The Guardian failed to restore health points")
    #                     return super().decrease_health(amount)
    #             else:
    #                 print(f"🛡️ Bonus : The Guardian restored {restore_roll} health points")
    #                 self._current_health += restore_roll

class Enforcer(Character): # Enforcer 
    # pass
   def decrease_health(self, amount):
    if (self._current_health - amount) < 0:
       amount = self._current_health
    else:
       coinThrow = randint(1, 4)
       if not coinThrow == 4:
           print("🐎 The Enforcer failed to gain defense as he's weakened by the Attacker")
       else:
           print("🐎 The Enforcer enrages and gain defense !")
           self._defense_value += 1
    self._current_health -= amount
    if (self._defense_value > 10):
        self._defense_value = 10
    self.show_healthbar()
       
class Shield_Master(Character):
   pass
