from Character import *

class Mage(Character):
    def compute_wounds(self, damages, roll, attacker):
        print(" Bonus: Magic armor (-3 wounds)")
        return super().compute_wounds(damages, roll, attacker) - 3