# la machine a pizaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

class pizza:
    def __init__(self, base, ingrédients, prix):
        self.base = base
        self.ingrédients = ingrédients
        self.prix = prix

calzone = pizza(base=['tomate'], ingrédients=['poulet', 'fromage', 'tomate'], prix=('20$'))
margarita = pizza(base=['tomate'], ingrédients=['tomate', 'fromage', 'basilic'], prix=('12$'))

print("bienvenu dans notre merveilleux restaurant, nous sommes ravis de vous acceuillir")
print("nous vous proposons deux pizza : la calzone et la margarita")

choix = input("quel pizza voulez vous ? ")

if choix == 'calzone':

    print("vous avez choisi la calzone")

    base = input("quel base voulez vous ? (tomate, sperme) ")

    calzone.base.remove('tomate')
    calzone.base.append(base)

    print(f"votre pizza a pour base {calzone.base}")

    ingredients = input(f"quel ingrédiente voulez vous ajouter ? (il y a actuellement ces ingrédients : {calzone.ingrédients})")

    calzone.ingrédients.append(ingredients)

    oui = input("souhaitez vous ajouter un autre ingrédiente ? (oui/non) ")

    if oui == "oui":
      ingredients = input(f"quel ingrédiente voulez vous ajouter ? (il y a actuellement ces ingrédients : {calzone.ingrédients})")
      calzone.ingrédients.append(ingredients)
      print(f"votre pizza a pour ingrédients {calzone.ingrédients}")

    elif oui == "non":
      print("ok, continuons")

    else:
      print("oui ou non uniquement, veuillez recommencer")
      exit()

    print(f"votre pizza a pour ingrédients {calzone.ingrédients}")
    print(f"votre pizza sera composée de {calzone.base} {calzone.ingrédients}")

    payement = input(f"le prix total est de {calzone.prix} souhaitez vous payer ? (oui/non) ")
    
    if payement == "oui":
      print("merci de votre achat")

    elif payement == "non":
      print("au revoir")
      exit()

    else:
      print("oui ou non uniquement, veuillez recommencer")
      exit()

    table = input("a quelle table vous les vous manger ? ")
    
    print(f"votre pizza sera prete dans 15 minute a la table n°{table}")

elif choix == 'margarita':

    print("vous avez choisi la margarita")

    base = input("quel base voulez vous ? (tomate, sperme) ")

    margarita.base.remove('tomate')
    margarita.base.append(base)

    print(f"votre pizza a pour base {margarita.base}")

    ingredients = input(f"quel ingrédiente voulez vous ajouter ? (il y a actuellement ces ingrédients : {margarita.ingrédients})")

    margarita.ingrédients.append(ingredients)

    oui = input("souhaitez vous ajouter un autre ingrédiente ? (oui/non) ")

    if oui == "oui":
      ingredients = input(f"quel ingrédiente voulez vous ajouter ? (il y a actuellement ces ingrédients : {margarita.ingrédients})")
      margarita.ingrédients.append(ingredients)
      print(f"votre pizza a pour ingrédients {margarita.ingrédients}")

    elif oui == "non":
      print("ok, continuons")
      
    else:
      print("oui ou non uniquement, veuillez recommencer")
      exit()

    print(f"votre pizza a pour ingrédients {margarita.ingrédients}")
    print(f"votre pizza sera composée de {margarita.base} {margarita.ingrédients}")

    payement = input(f"le prix total est de {margarita.prix} souhaitez vous payer ? (oui/non) ")
    
    if payement == "oui":
      print("merci de votre achat")

    elif payement == "non":
      print("au revoir")
      exit()

    else:
      print("oui ou non uniquement, veuillez recommencer")
      exit()

    table = input("a quelle table vous les vous manger ? ")
    
    print(f"votre pizza sera prete dans 15 minute a la table n°{table}")

else:
    print("pizza non proposée dans ce restaurant")
    
