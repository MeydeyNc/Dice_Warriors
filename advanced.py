from __future__ import annotations
import time 

from Conf import set_conf

def ask_user(question:str):
    value = input(question)
    
    if type(value) is not str:
        print("Illegal input !")
        return ask_user(question)
    
    try:
        value = int(value)
    except :
        print("Entrer int value !")
        return ask_user(question)
    
    return value if value > 2 else ask_user(question + " ( > 2 ) :   ")


if __name__ == "__main__":
    set_conf(False)
    try:
        exec(open("main.py").read())
    except KeyboardInterrupt :
        set_conf(True)
        raise KeyboardInterrupt("A head smashed your keyboard ...")
    set_conf(True)
