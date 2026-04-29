import os
import time

class Vie:
    def __init__(self):
        self.vie = 3
        self.score = 0

    def bonnerep(self):
        self.score += 1 #on ajoute 1 score pour une bonne réponse += veux dire ajouté 

    def mauvaiserep(self):
        self.vie -= 1 #On retire une vie quand on mais une mauvaise réponse avec -= qui signifie retiré 1 sur la somme de vie qui et = a 3 par default

mavie = Vie() # ma variable pour relier la class et pouvoir l'utilisé dans mo ncode 

player = Vie() # pareil que au desus

print(
    "Qui est le plus intelligent ? ",
    "Réponse 1 : Toi",
    "Réponse 2 : Moi"
)

reponse = input("Répond A la premier questions : ")

if reponse == "2":
    mavie.bonnerep()
    print("Bienjouer tu a gagnez")
else:
    mavie.mauvaiserep()
    print("Tu a perdu...")
    


time.sleep(2) # On attends 2 Seconds
os.system("cls") # Demander a windows de suprimé la terminals fin ce qui a marqué dedant

print("Qui gagnerait un combat ? ")
print("Réponse 1 : Lion")
print("Réponse 2 : Tigre")

deuxieme = input("Répond a la question : ")

if deuxieme == "1":
    mavie.bonnerep()
    print("Tu a reussi")
else: 
    mavie.mauvaiserep()
    print("Ta perdu domage")

time.sleep(2)
os.system("cls")

print("Quesqui et gros et imposant")
print("1. Ma bite")
print("2. Ta pute de mère")

troisieme = input("Répond a la question : ")

if troisieme == "2":
    mavie.bonnerep()
    print("Bienjouer !")
else:
    mavie.mauvaiserep()
    print("Tu a perdu tdc")


print("Score :", mavie.score)
print("Vie Restante :", mavie.vie)
