# TANK : 

### Paladin : 
   - Obtiens de base une défense plus grande grâce à sa foi. 
   - Pour le Paladin, on v aimplémenter la notion du dé pour le monsieur. 
   - Dé 4 : 
     - 1 : wounds - 3
     - 2 : attaque augmentée
     - 3 : défense augmentée
     - 4 : Self heal

### Leviathan : 
 - Peut attirer l'attention et éviter les coups 
 - Comment il évite les coups ?  
    - On augmente sa défense sur un jet de dé ou sur une base fixe ? 
    Jet de dé sur un 6 : attaque annulée
    Dé 1 : prend toute l'attaque 
    Jet intermédiaire : on voit réduire l'attaque par rapport au dé // On divise l'attaque par 2

### Guardian : 
   - Un sac à pv qui restaure de la vie en fonction des dégâts pris. 
      - On peut faire un jet de dé pour savoir si on restaure de la vie ou pas.
      - On peut faire un jet de dé pour savoir combien de vie on restaure.

      On va avoir un bool qui va nous dire si on a pris des dégâts ou pas.
      Si on a pris des dégâts, on lance un dé pour savoir si on restaure de la vie ou pas.
      Si on restaure de la vie, on lance un dé pour savoir combien de vie on restaure.

### Steel_Cavalier ( Ou Enforcer ):
   - On veut un tank qui en fonction des dégâts pris va augmenter sa valeur de défense. 
      - On peut faire un jet de dé pour savoir si on augmente la défense ou pas.
      - On augmente sa défense en fonction des dégâts pris.  
         - Comment on peut faire ça en calcul ? On utilise du pourcentage en fonction de la vie restante et de la défense ?  
