# Python

```
try:
  python_ces_quoi = input("Sais quoi python pour toi ? : ").lower()
except ValueError as e:
  print(f"Error {e}")
try:
  if python_ces_quoi == "Le meileur":
    print(python_ces_quoi, "Alors veux tu apprendre python maitenant que tu en connais les capacité ?")
  else:
      print(python_ces_quoi, "Bon bah Bonne journée passe ton chemin :)")
except Exception as e:
  print(f"Error {e}")
```
# Good luck !
