
def set_Character(bool: bool):
    choix_premier_bloc = bool
    chemin_fichier_source = 'Character.py'
    with open(chemin_fichier_source, 'r', encoding='utf-8') as source_file:
        lignes_source = source_file.readlines()

    if choix_premier_bloc:
        nouveau_bloc = [
            '\n'
            '\n'
            '\n'
            'class Character:'
            '\n'
            '    _max_health = randint(18, 22)\n',
            '    _current_health = _max_health\n',
            '    _attack_value = randint(7, 13)\n',
            '    _defense_value = randint(2, 5)\n'
        ]
    else:
        nouveau_bloc = [
            'from advanced import ask_user'
            '\n'
            '\n'
            'class Character:'
            '\n'
            '    _max_health = ask_user("Choose default max health value :   ")\n',
            '    _current_health = _max_health\n',
            '    _attack_value = ask_user("Choose default attack value, def will be attack/3 :   ")\n',
            '    _defense_value = round(_attack_value / 3) + randint(-2, 3)\n'
            '\n'
        ]

    nouvelles_lignes_source = lignes_source[:4] + nouveau_bloc + lignes_source[12:]

    with open(chemin_fichier_source, 'w', encoding='utf-8') as source_file:
        source_file.writelines(nouvelles_lignes_source)
        
def set_Team(bool: bool):
    choix_premier_bloc = bool
    chemin_fichier_source = 'Team.py'
    with open(chemin_fichier_source, 'r', encoding='utf-8') as source_file:
        lignes_source = source_file.readlines()

    if choix_premier_bloc:
        nouveau_bloc = [
            '\n'
            'class Team:'
            '\n'
            '\n'
            '    _game_dice = randint(4,9)\n'
            '    _max_instances = 1\n'
            '    _team_len = randint(1,5)* _max_instances\n'
        ]
    else:
        nouveau_bloc = [
            'from advanced import ask_user'
            '\n'
            '\n'
            'class Team:'
            '\n'
            '    _game_dice = ask_user("Choose game dice :   ")\n',
            '    _max_instances = 1\n',
            '    _team_len = ask_user("Choose team length :   ")\n',
        ]

    nouvelles_lignes_source = lignes_source[:6] + nouveau_bloc + lignes_source[12:]

    with open(chemin_fichier_source, 'w', encoding='utf-8') as source_file:
        source_file.writelines(nouvelles_lignes_source)
        
def set_conf(bool: bool):
    set_Character(bool)
    set_Team(bool)
    
if __name__ == "__main__":
    exec(open("main.py").read())
