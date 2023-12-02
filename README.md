# 🎲 Bienvenue sur Dice Warriors ! 🎲


Ceci est un autobattler en équipe réalisé dans le cadre d'un projet Python encadré par Monsieur G.Ladrat. 


## Première utilisation. 

#### 1. Télécharger et/ou cloner notre [répo](https://github.com/MeydeyNc/Dice_Warriors.git)

#### 2. Initialiser et installer l'environnement grâce au fichier 'requirements.txt' : 
*Vous pourrez utiliser la commande suivante afin de configurer tout l'environnement nécessaire à la bonne utilisation de notre jeu :* 
````
pip install -r requirements.txt
```` 
#### 3. Vous aurez ici deux choix de modes de jeu ! 

 - **Le Mode Normal : Se glisser dans le main.py et lancer le script via l'exécuteur Python !**

 - **Le *Mode Advanced* : Se glisser dans [advanced.py](advanced.py) et lancer le script via l'exécuteur Python !**

### Le ***Mode Advanced*** permet une certaine personnalisation de l'expérience de jeu : 
 - **Un choix libre de différentes valeurs :** 
      - Une valeur max par défaut pour la vie des personnages.
      - Une valeur d'attaque par défaut.
      - Un dé (4, 6, 10, 20, 100)
      - La taille des équipes qui s'affrontent.

#### Vous aurez 2 catégories de classes qui seront choisies au hasard dans 2 équipes d'une taille aléatoire qui s'affronteront.

*Nous avons pu implémenter diverses aptitudes basées sur des "roll", ou lancés de dés, déterminant ainsi :* 
   - *une réussite critique : la plus grande face du dé ;* 
   - *un échec critique : la plus petite face du dé*.

## Les Tanks : 

####  Le Paladin : 
   - Qui peut lancer diverses aptitudes au cours du combat : 
      - Grâce à sa foi, il peut obtenir une résistance de 3 aux dégâts. 
      - Renforcer sa défense.
      - Renforcer son attaque.
      - Se soigner.
     
#### Le Phantom_Warden : 
 - Grâce à son aspect fantomatique, le Phantom peut :
   - Sur une réussite critique esquiver complètement une attaque. 
   - Sur un échec critique prendre le double de dégâts anticipé.
   - Sur un jet plus classique esquiver la moitié des dégâts.

#### Le Leviathan : 
   - Un puissant personnage comptant sur son endurance naturelle : 
      - Sur un premier lancer de pièce décide si oui ou non un roll pour regagner de la vie est lancé, sinon ne regagne pas de vie.
         - Sur une réussite critique le Leviathan restorera un montant égal à la plus haute face du dé.
         - Sur un jet classique le personnage reprendra autant de vie que la valeur de la face tombée.

#### Le Guardian:
   - Le Guardian est une ligne de défense solide gagnant de la résistance à chaque coup reçus. 
      - On va faire un premier jet de dé pour savoir si oui ou non le Guardian se renforcera ou non.
      - On augmentera alors sa défense (de 2) ou non.  

#### Le Shield_Master : 
 - Un maître de la parade arrivé il y a peu d'une terre ingrate ou les seigneurs des cendres et les âmes noires rôdent. 
   - Sur une réussite critique le Shield_Master renverra la totalité des dégâts à son agresseur.
   - Sur un jet plus classique, il divisera les dégâts pris par la valeur de son roll.
   - Enfin sur un échec critique celui-ci prendra les dégâts dans leurs entièreté.
      - un être sorti tout droit de l'imagination de Miyazaki.


## Les DPS ou Attackers :
 *(DPS : Damage Per Seconds // Dommages Par Secondes)*

#### Le Warrior : 
   - Frappe plus fort qu'un Lopez. 
      - Sur une réussite critique, il augmente les dégâts qu'il inflige. 
      - Sur un échec critique, le Warrior se reçoit son épée dans la figure. 

#### Le Thief : 
   - Un petit malin passant à travers l'armure de ses adversaires, mais pas que !
      - En tout temps le Thief passera à travers l'armure de ses adversaires.
      - Sur une réussite critique le Thief volera également des points de vie afin de restaurer les siens.
      - Mais attention, sur un échec critique il perdra de la capacité à voler la vie des autres, chéh. 

#### Le Berserker : 
   - Venu tout droit du folklore nordique, le Berserker prendra quelques champignons avant la bataille, rien de toxique rassurez-vous.
      - Tant que le Berserker est en vie, il représente une menace : ses dégâts augmenteront à chaque blessure. 
      - Sur une réussite critique comme son compère Warrior, il doublera ses dégâts infligés.
      - Sur un échec critique, il perdra de sa hargne et s'affaiblira. 

#### Le Samurai : 
   - Venu de l'Est, ce combattant à la technique redoutable peut infliger des blessures sévères et douloureuses.
      - Sur un bon jet, le Samurai laisse des marques et inflige une hémorragie sur plusieurs tours drainant ainsi les points de vie de ses adversaires.
      - Sur un échec critique, celui-ci s'infligera, de honte, des blessures afin de ne pas oublier son erreur.


#### Le Mage : 
   - Puissant maître de la magie, il est votre meilleur ami et pire ennemi. 
      - Chaque tour canalisant sa magie, il enverra sa plus puissante attaque s'écraser contre ses adversaires, réduisant l'armure la plus épaisse à l'état de cendres.
      - Sur un mauvais jour cependant, un coup de grisou viendra lui épousseter la moustache. 

-------



Nous espérons que ce petit jeu plaira ! 

Signé : Lyse LEBOURCQ, Mathieu BARBOTEAU & Mederic MARQUIE.