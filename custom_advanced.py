from Conf import set_Character

if __name__ == "__main__":
    set_Character(False)
    try:
        exec(open("custom.py").read())
    except KeyboardInterrupt :
        set_Character(True)
        print("Game stopped")
    set_Character(True)