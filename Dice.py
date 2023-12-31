import random

class Dice:
    
    def __init__(self, faces=6):
        self._faces = 2 if faces <= 2 else faces
        
    def __str__(self):
        return f"I'm a {self._faces} faces dice"
    
    def roll(self):
        return random.randint(1, self._faces)

      
class RiggedDice(Dice):
    
    def roll(self, rigged=False):
        return self._faces if rigged else super().roll()


if __name__ == "__main__":
    exec(open("main.py").read())
