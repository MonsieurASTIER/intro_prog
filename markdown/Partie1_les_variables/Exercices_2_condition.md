# Validons nos nouvelles connaissances
Pour rappel ces QCM ne sont pas notés, mais sert à auto-évaluer votre compréhension du cours. Prenez donc le temps de répondre comme il faut au questions et de relire le cours si besoin.


Les variables a,b,c sont définie comme ci-dessous
```python
a=10
b,c = 8,2
```

?[1. l'instruction a<8 renveras:]
- [X] True
- [] False


?[2. l'instruction a<b renveras:]
- [] True
- [X] False

?[3. l'instruction a>b and a>c renveras:]
- [X] True
- [] False

?[4. l'instruction a<b and b>c renveras:]
- [X] True
- [] False

?[5. l'instruction True and False renveras:]
- [] True
- [X] False


```
a,b,c = 10,8,2
if a>b:
  if a>c:
    print("A")
  else:
    print("C")
else:
    print("B")
```

?[6. Qu'affiche le programme ci-dessus]
-[X] "A"
-[] "C"
-[] "B"
-[] affiche rien



```
a,b,c = 10,8,2
if a < b + c:
  if a > c:
    print("A")
  else:
    print("C")
else:
    print("B")
```

?[7. Qu'affiche le programme ci-dessus]
-[] "A"
-[] "C"
-[X] "B"
-[] affiche rien


```
a,b,c = 10,8,2
if a < b :
  if a > c:
    print("A")
  else:
    print("C")
elif a<c:
    print("B")    
```

?[8. Qu'affiche le programme ci-dessus]
-[] "A"
-[] "C"
-[] "B"
-[x] affiche rien

```
a,b,c = 10,8,2
if a < b and a > c:
  print("B")
elif a > b and a < c:
  print("C")
else:
  print("A")
```

?[9. Qu'affiche le programme ci-dessus]
-[X] "A"
-[] "C"
-[] "B"
-[] affiche rien


?[10. Que fait le programme ci-dessus]
-[] il affiche le nom de la variable contenant la plus grande valeur
-[] il affiche le nom de la variable contenant la plus petite valeur
-[] il affiche le nom d'une variable aléatoire
-[X] Ce code ne fait rien de spécial


```
a,b,c = 10,8,2
if a < b and a > c:
  print("B")
elif a > b and a < c:
  print("C")
elif a<b and a<c and b<c:
    print("C")
elif a<b and a<c:
    if c<b:
      print("B")
else:
    print("A")
```

?[11. Qu'affiche le programme ci-dessus]
-[X] "A"
-[] "C"
-[] "B"
-[] affiche rien


?[12. Que fait le programme ci-dessus]
-[X] il affiche le nom de la variable contenant la plus grande valeur
-[] il affiche le nom de la variable contenant la plus petite valeur
-[] il affiche le nom d'une variable aléatoire
-[] Ce code ne fait rien de spécial

```
a="A"
if "a" == "A":
  print("a")
elif a == "a":
  print("b")
elif a == "A":
    print("C")
```

?[11. Qu'affiche le programme ci-dessus]
-[] "A"
-[] "B"
-[X] "C"
-[] affiche rien




## On complique un peu les choses
```
a,b,c = 10,8,2
if (a < b and a > c) or True:
  print("B")
else:
    print("A")
```

?[13. Qu'affiche le programme ci-dessus]
-[] "A"
-[] "C"
-[X] "B"
-[] affiche rien


```
a,b,c = 10,8,2
if (a < b and a > c) or (a<=10 or b>c):
  print("B")
else:
    print("A")
```

?[14. Qu'affiche le programme ci-dessus]
-[] "A"
-[X] "B"
-[] "C"
-[] affiche rien



```
a,b,c = 10,8,2
if (a < b and a > c) and (a <= 10 or b > c) and (a > b):
  print("B")
else:
    print("A")
```

?[15. Qu'affiche le programme ci-dessus]
-[x] "A"
-[] "B"
-[] "C"
-[] affiche rien

```
if ((a < b) ^ (a > c)) and ( a+2 > b-2):
  print("B")
else:
    print("A")
```

?[16. Qu'affiche le programme ci-dessus]
-[] "A"
-[X] "B"
-[] "C"
-[] affiche rien





# Programme:
Ecrire sur votre IDE les différents programmes:


**Programme 1:**
Le programme de la question 12 est mal ecrit, certaine condition sont redondante, et il ne prend pas en compte tout les cas de figures (égalité ect)
Réecrire le programme de la question 12 qui renvoie la plus grnade valeur et son nom de variable. En cas d'égalité afficher une deux des variables.


**Programme 2:**
Récrire le programme du calcule du pain, mais désormais l'utilisateur devra saisir le nombre de pain acheter ainsi que le type de pain.

__Astuce vous pouvez afficher un choix multiple à l'utilisateur en proposant une saisie précise:__
__1.Pour une baguette tapper 1__
__2.Pour des croissant taper 2...__
