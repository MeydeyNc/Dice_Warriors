from Character import *
from dataclass import Buff
from random import randint

class Paladin(Character):
   buff: Buff = Buff(randint(10, 40), randint(1, 6), randint(5, 20))
   def compute_wounds(self, damages, roll, attacker):
       print("🔨 Bonus: Holy armor (-3 Wounds)")
       return super().compute_wounds(damages, roll, attacker) - 3
   
class Leviathan(Character):
   buff: Buff = Buff(randint(10, 40), randint(1, 6), randint(5, 20))
   def compute_wounds(self, damages, roll, attacker):
       roll: int = self._dice.roll()
       if (roll == 6):
           print("🐙 Bonus : The Leviathan slipt throught the attack ! (Wounds / 2)")
           return super().compute_wounds(damages, roll, attacker) / 2   
       elif (roll == 1):
           print("🐙 Malus : The Leviathan missed is escape ... (Wounds x 2)")
           return super().compute_wounds(damages, roll, attacker) * 2
       else:
           print(f"🐙 Bonus : The Leviathan evaded the attack ! (Wounds - {roll})")
           return super().compute_wounds(damages, roll, attacker) - roll

class Guardian(Character):
   pass

class Steel_Cavalier(Character):
   pass

class Shield_Master(Character):
   pass
