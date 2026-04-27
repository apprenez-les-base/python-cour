# 📘 Cours Python

---

## 🔹 Bases

```python
print("hello, world")
```

### Variables

```python
entier = 20
string = "hello"
flottant = 1.2
```

### Exemples

```python
print(entier + flottant)        # 21.2
print(str(entier) + string)     # "20hello"
```

---

## 🔹 Input utilisateur

```python
age = input("Entre ton âge : ")
print(age)
```

```python
age = int(input("Entre ton âge : "))
print(age)
```

```python
print(age, type(age))
```

---

## 🔹 Projet 1 : Celsius → Fahrenheit

```python
celsius = float(input("Entrez votre température en celsius : "))
fahrenheit = celsius * 9 / 5 + 32

print(celsius, "degrés celsius équivalent à", fahrenheit, "degrés fahrenheit")
```

---

## 🔹 Booléens

```python
print(bool(1))   # True
print(bool(0))   # False
```

---

## 🔹 Comparaisons

```python
print(2 < 3)   # True
print(2 < 1)   # False
print(2 < 3 and 3 > 1)
```

---

## 🔹 Conditions

```python
mdp = input("Quel est ton mot de passe : ")

if mdp == "1234":
    print("Mot de passe correct")
else:
    print("Mot de passe incorrect")

print("Fin du programme")
```

### Vérification complète

```python
if len(mdp) < 5:
    if len(mdp) == 0:
        print("Il faut entrer un mot de passe")
    else:
        print("Mot de passe trop court")
elif mdp == "12345":
    print("Mot de passe correct")
else:
    print("Mot de passe incorrect")

print("Fin du programme")
```

---

## 🔹 Projet 2 : Mention bac

```python
moyenne = float(input("Entrer votre moyenne : "))

if 12 <= moyenne < 14:
    print("Mention assez bien")
elif 14 <= moyenne < 16:
    print("Mention bien")
elif 16 <= moyenne <= 20:
    print("Mention très bien")
elif moyenne >= 18:
    print("Mention très bien avec félicitations du jury")
else:
    print("Pas de mention")
```

---

## 🔹 Listes

```python
liste = [42, 'abc', 1.1, 30]

liste[0] = 1
print(liste[0:3])

liste.append(1337)
liste.remove(1.1)

print(liste)

print('b' in ['a', 'b', 'c'])  # True
```

---

## 🔹 Boucles

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

```python
for lettre in ['a', 'b']:
    print(lettre)
```

```python
for i in range(5):
    print(i)
```

---

## 🔹 Projet 3 : Jeu du mot

```python
vie = 7
mot = "code"
pb = "_" * len(mot)

while vie > 0 and mot != pb:
    lettre = input("Entrez une lettre : ")

    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                pb = pb[:i] + lettre + pb[i + 1:]
    else:
        vie -= 1

    if pb == mot:
        print("Félicitations, vous avez gagné !")
    elif vie == 0:
        print("Vous avez perdu !")
    else:
        print("Il vous reste", vie, "vies")
```

---

## 🔹 Fonctions

```python
def fonction(*args):
    print(args)

fonction(5, 4)
```

```python
def fonction_kwargs(**kwargs):
    print(kwargs)

fonction_kwargs(cinq=5, quatre=4)
```

```python
def somme(a, b):
    return a + b, a, b

s = somme(4, 5)
print(s)
```

---

## 🔹 Projet 4 : simple_range

```python
def simple_range(n):
    l = []
    i = 0

    while i < n:
        l.append(i)
        i += 1

    return l

print(simple_range(5))
```
