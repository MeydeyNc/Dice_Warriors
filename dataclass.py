from dataclasses import dataclass

@dataclass 
class Buff:
    _max_health: int = 40
    _attack_value: int = 5
    _defense_value: int = 8
    
    