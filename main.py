import os

python_ces_quoi = os.getenv("QUESTION")

if python_ces_quoi is None:
    python_ces_quoi = input("Sais quoi python pour toi ? : ")

if python_ces_quoi == "Le meileur":
    print(python_ces_quoi, "Alors veux tu apprendre python maintenant que tu en connais les capacités ?")
else:
    print(python_ces_quoi, "Bon bah Bonne journée passe ton chemin :)")
