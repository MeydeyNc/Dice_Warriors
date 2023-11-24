from dataclasses import dataclass

@dataclass 
class Buff:
    _max_health: int = 20
    _attack_value: int = 5
    _defense_value: int = 3
    
    