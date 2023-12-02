from Conf import set_Character

if __name__ == "__main__":
    set_Character(False)
    try:
        exec(open("custom.py").read())
    except KeyboardInterrupt :
        set_Character(True)
        raise KeyboardInterrupt("A head smashed your keyboard ...")
    set_Character(True)