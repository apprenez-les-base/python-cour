# Random voila voila petit jeux 
# Faite vous plaiz 
# Si vous aimer les truc dans le genre ditent le en issues comme ca jen fais plus ;) avec autant d'éxplication


import random # seuls random car on utiilise que random voila importer os si entre chaque manche vous voulez cls des truc je vous le mais en commentaire ;)
# import os

class vie: # on crée une class pour le score et la vie 
    def __init__(self): 
        self.Chance = 3 # on mais que ya que 3chance 
        self.score = 0 # le score commence a 0 
    def mauvaiserep(self): 
        self.Chance -= 1 # si on mais une mauvaise rep on  enleve une vie 
    def score(self):
        self.score += 1 # si on gagne on ajoute 1s de score

lavie = vie() # on crée notre variable pour demandé la class vie pour pas avoir a fair self.chance voila comme ca on fais lavie.chance


while lavie.Chance > 0: # on crée une boucle jusqua avoir 0 vie 
    
    choisis = int(input("Choisis un chiffre : ")) # on demande a l'utilisateur d'écrire

    chiffre = random.randint(0, 90) # on genere un chiffre aleatoirement de 0 a 90

    if chiffre == choisis: # on donne une condition si le chiffre et bon ca ajoute 1 au score et ca nous dis bienjouer 
        lavie.score()
        print("Bienjouer tu a gagnez")
       # os.system("cls")
    else: # si la condition si desus et pas respecté donc on a pas gagnez ca nous dis le chifre et nous retire une vie 
        lavie.mauvaiserep()
        print("Ta perdu sale merde le chiffre etais", chiffre)
       # os.system("cls")
print("Il te reste", lavie.Chance) # on mais le nombre de chance qu'il nous restez 
print("Tu a fais ce score", lavie.score) # puis le score qu'on a fais voila :)
