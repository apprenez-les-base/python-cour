# 📘 Le Guide Complet Python de Light

Bienvenue dans ce guide ! J'ai regroupé ici tout mon parcours d'apprentissage, mes projets et mes notes pour aider n'importe quel débutant à se lancer. Bonne lecture ! 🚀

---

## 🔹 1. Les Bases : Affichage et Variables
C'est ici que tout commence. On apprend à parler à l'ordinateur.

```python
print("hello, world")

entier = 20
string = "hello"
flottant = 1.2
```
**Explication :**
- `print()` : Sert à afficher du texte ou des chiffres dans la console.
- **Variables** : C'est comme des boîtes où on stocke des infos. On a des **entiers** (chiffres ronds), des **strings** (texte entre guillemets) et des **flottants** (chiffres à virgule).

```python
print(entier + flottant)        # Résultat : 21.2
print(str(entier) + string)     # Résultat : "20hello"
```
**Explication :**
- On peut additionner des chiffres.
- `str(entier)` : On transforme le chiffre en texte pour pouvoir le coller à un autre texte (on appelle ça la concaténation).

---

## 🔹 2. Input : Parler avec l'utilisateur
Le programme nous pose des questions.

```python
age = input("Entre ton âge : ")
age_entier = int(input("Entre ton âge : "))
print(age_entier, type(age_entier))
```
**Explication :**
- `input()` : Ouvre une zone de texte pour que l'utilisateur réponde. **Attention**, par défaut, la réponse est toujours considérée comme du texte (String).
- `int()` ou `float()` : On force la réponse à devenir un chiffre pour pouvoir faire des calculs avec.

---

## 🔹 3. Projet n°1 : Convertisseur Celsius → Fahrenheit
Mon premier vrai petit outil.

```python
celsius = float(input("Entrez votre température en celsius : "))
fahrenheit = celsius * 9 / 5 + 32

print(celsius, "degrés celsius équivalent à", fahrenheit, "degrés fahrenheit")
```
**Explication :**
- On récupère un chiffre à virgule (`float`).
- On applique une formule mathématique.
- On affiche le résultat de façon élégante.

---

## 🔹 4. La Logique et les Comparaisons
Comment Python prend des décisions.

```python
print(bool(1))   # True (vrai)
print(bool(0))   # False (faux)

print(2 < 3)   # True
print(2 < 3 and 3 > 1) # True (les deux doivent être vrais)
```
**Explication :**
- **Booléens** : C'est soit Vrai (`True`), soit Faux (`False`). 
- **Opérateurs** : `<` (plus petit), `>` (plus grand), `==` (égal), `!=` (différent).
- **and / or** : Permettent de vérifier plusieurs conditions à la fois.

---

## 🔹 5. Les Conditions (If / Elif / Else)
Le cœur de la programmation.

```python
mdp = input("Quel est ton mot de passe : ")

if len(mdp) < 5:
    print("Trop court !")
elif mdp == "12345":
    print("Correct")
else:
    print("Incorrect")
```
**Explication :**
- `if` : "Si cette condition est vraie, fais ça".
- `elif` : "Sinon, si cette AUTRE condition est vraie, fais ça".
- `else` : "Dans tous les autres cas, fais ça".
- `len()` : Sert à compter le nombre de caractères dans un texte.

---

## 🔹 6. Projet n°2 : Gestionnaire de Mentions au Bac
Un exemple concret d'utilisation des conditions.

```python
moyenne = float(input("Entrer votre moyenne : "))

if 12 <= moyenne < 14:
    print("Mention assez bien")
elif 14 <= moyenne < 16:
    print("Mention bien")
elif 16 <= moyenne <= 20:
    print("Mention très bien")
else:
    print("Pas de mention ou échec")
```
**Explication :**
- On utilise `elif` pour tester plusieurs tranches de notes les unes après les autres.

---

## 🔹 7. Les Listes
Pour stocker plein d'informations dans une seule variable.

```python
liste = [42, 'abc', 1.1]
liste.append(1337) # Ajoute à la fin
liste.remove('abc') # Enlève l'élément
print(liste[0]) # Affiche le premier élément (on commence à 0 !)
```
**Explication :**
- Une liste se crée avec des crochets `[]`.
- `.append()` : On rajoute un objet dans la "boîte".
- `.remove()` : On enlève un objet.
- **Index** : Le premier objet est à la position `0`, le deuxième à `1`, etc.

---

## 🔹 8. Les Boucles (While et For)
Pour répéter des actions automatiquement.

```python
# Boucle WHILE
i = 0
while i < 5:
    print(i)
    i += 1

# Boucle FOR
for i in range(5):
    print(i)
```
**Explication :**
- `while` : Continue tant que la condition est vraie. Attention à ne pas oublier le `i += 1` sinon la boucle est infinie !
- `for` : Très pratique pour parcourir une liste ou une `range()` (une suite de nombres).

---

## 🔹 9. Projet n°3 : Le Jeu du Pendu (Simplifié)
Un gros morceau qui utilise boucles et listes.

```python
vie = 7
mot = "code"
pb = "_" * len(mot) # Affiche ____

while vie > 0 and mot != pb:
    lettre = input("Entrez une lettre : ")
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                pb = pb[:i] + lettre + pb[i + 1:]
    else:
        vie -= 1
    print(pb, "| Vies restantes :", vie)
```
**Explication :**
- On remplace les tirets `_` par la lettre si elle est dans le mot.
- On retire une vie si on se trompe.
- La boucle s'arrête quand on gagne (plus de `_`) ou qu'on perd (0 vie).

---

## 🔹 10. Les Fonctions
Pour créer ses propres outils réutilisables.

```python
def somme(a, b):
    return a + b

resultat = somme(10, 5)
print(resultat)
```
**Explication :**
- `def` : On définit une fonction.
- `return` : C'est ce que la fonction "donne" à la fin de son travail.

---

## 🔹 11. Tuples, Ensembles et Dictionnaires
Les autres façons de stocker des données.

```python
mon_tuple = (1, 2, 3) # Non modifiable
mon_set = {1, 2, 2, 3} # Pas de doublons (affichera {1, 2, 3})
mon_dico = {"nom": "Light", "age": 20} # Système de Clé: Valeur
```
**Explication :**
- **Tuple** : Pour des données qui ne doivent jamais changer.
- **Set** : Pour s'assurer qu'il n'y a pas deux fois la même chose.
- **Dico** : Très puissant pour l'organisation (ex: `mon_dico["nom"]` donnera "Light").

---

## 🔹 12. Les Classes (Programmation Orientée Objet)
C'est le niveau supérieur : on crée nos propres types d'objets.

```python
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

    def klaxonner(self):
        print("Bip Bip !")

ma_caisse = Voiture("Tesla", 2023)
print(ma_caisse.marque)
ma_caisse.klaxonner()
```
**Explication :**
- `class` : C'est le plan de construction.
- `__init__` : C'est ce qui se passe quand on "construit" l'objet (on lui donne ses caractéristiques).
- `self` : C'est le mot-clé pour que l'objet parle de lui-même.

---

## 🔹 13. Dernières Astuces & Sécurité
Ce qu'on a appris récemment.

- **`eval()`** : Calcule une string (ex: `eval("2*3")`). **DANGER** : Ne jamais l'utiliser avec des données qu'on ne contrôle pas, car on peut pirater ton ordi avec.
- **`exit()`** : Pour fermer le programme proprement.
- **`AttributeError`** : Une erreur courante quand on se trompe de type (ex: vouloir `.append()` sur du texte).

---

## 🍕 Projet Final : La Machine à Pizza (Projet n°5)
C'est le projet le plus complet. Il mélange classes, listes, conditions et gestion d'erreurs.

```python
class pizza:
    def __init__(self, base, ingrédients, prix):
        self.base = base
        self.ingrédients = ingrédients
        self.prix = prix

calzone = pizza(base=['tomate'], ingrédients=['poulet', 'fromage'], prix='20$')

print("Bienvenue !")
choix = input("Quelle pizza voulez-vous ? ")

if choix == 'calzone':
    # Changement de base
    nouvelle_base = input("Quelle base ? ")
    calzone.base.remove('tomate')
    calzone.base.append(nouvelle_base)
    
    # Ajout d'ingrédient
    sup = input(f"Ajouter un ingrédient ? (actuellement: {calzone.ingrédients}) ")
    calzone.ingrédients.append(sup)
    
    # Gestion d'erreur (Oui/Non)
    encore = input("Encore un ? (oui/non) ")
    if encore == "non":
        print("Ok !")
    elif encore != "oui":
        print("Erreur !")
        exit() # On arrête tout si la réponse est invalide
    
    print(f"Prix : {calzone.prix}. Table ?")
    table = input("Numéro de table : ")
    print(f"C'est prêt pour la table {table} !")
```
**Explication du Projet Final :**
1. **La Classe `pizza`** : Elle permet de créer autant de modèles de pizzas qu'on veut avec leurs propres listes d'ingrédients.
2. **Les Listes** : On utilise `.remove()` et `.append()` pour modifier la pizza en direct selon les envies du client.
3. **Le `if/elif/else`** : Indispensable pour gérer le menu et les réponses de l'utilisateur.
4. **Le `exit()`** : On l'utilise comme une sécurité : si l'utilisateur ne suit pas les consignes, on ferme le programme pour éviter les bugs.

---

**Félicitations !** Si tu as lu jusque là et que tu as testé les codes, tu as les bases solides pour devenir un vrai développeur Python. La clé, c'est de pratiquer ! 👨‍💻👩‍💻
