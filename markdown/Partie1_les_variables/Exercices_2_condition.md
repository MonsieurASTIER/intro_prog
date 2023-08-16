# Validons nos nouvelles connaissances
Pour rappel, ces QCM ne sont pas notés, mais servent a autoévaluer votre compréhension du cours. Prenez donc le temps de répondre comme il faut aux questions et de relire le cours si besoin.


Les variables a,b,c sont défini comme ci-dessous.
```python
a = 10
b,c = 8,2
```

?[1. Que renvoie l'instruction (a<8) :]
- [] True
- [X] False

?[2. Que renvoie l'instruction (a<b) : ]
- [] True
- [X] False

?[3. Que renvoie l'instruction (a>b and a>c) :]
- [X] True
- [] False

?[4. Que renvoie l'instruction (a-2 != b) :]
- [] True
- [x] False

?[5. Que renvoie l'instruction (True and False) :]
- [] True
- [X] False

***
***

```python
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
-[] "B"
-[] "C"
-[] affiche rien

***
***

```python
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
-[X] "B"
-[] "C"
-[] affiche rien

***
***

```python
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
-[] "B"
-[] "C"
-[x] affiche rien

***
***

```python
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
-[] "B"
-[] "C"
-[] affiche rien


?[10. Que fait le programme ci-dessus]
-[] il affiche le nom de la variable contenant la plus grande valeur
-[] il affiche le nom de la variable contenant la plus petite valeur
-[] il affiche le nom d'une variable aléatoire
-[X] Ce code ne fait rien de spécial

***
***

```python
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
-[] "B"
-[] "C"
-[] affiche rien


?[12. Que fait le programme ci-dessus]
-[X] il affiche le nom de la variable contenant la plus grande valeur
-[] il affiche le nom de la variable contenant la plus petite valeur
-[] il affiche le nom d'une variable aléatoire
-[] Ce code ne fait rien de spécial

***
***

```python
a="A"
if "a" == "A":
  print("a")
elif a == "a":
  print("b")
elif a == "A":
    print("C")
```

?[13. Qu'affiche le programme ci-dessus]
-[] "A"
-[] "B"
-[X] "C"
-[] affiche rien




## On complique un peu les choses

```python
a,b,c = 10,8,2
if (a < b and a > c) or True:
  print("B")
else:
    print("A")
```

?[14. Qu'affiche le programme ci-dessus]
-[] "A"
-[X] "B"
-[] "C"
-[] affiche rien

***
***

```python
a,b,c = 10,8,2
if (a < b and a > c) or (a<=10 or b>c):
  print("B")
else:
    print("A")
```

?[15. Qu'affiche le programme ci-dessus]
-[] "A"
-[X] "B"
-[] "C"
-[] affiche rien

***
***

```python
a,b,c = 10,8,2
if (a < b and a > c) and (a <= 10 or b > c) and (a > b):
  print("B")
else:
    print("A")
```

?[16. Qu'affiche le programme ci-dessus]
-[x] "A"
-[] "B"
-[] "C"
-[] affiche rien

***
***

```python
if ((a < b) ^ (a > c)) and ( a+2 > b-2):
  print("B")
else:
    print("A")
```

?[17. Qu'affiche le programme ci-dessus]
-[] "A"
-[X] "B"
-[] "C"
-[] affiche rien




# Programme :
Écrire sur votre IDE les différents programmes :


**Programme 1:**
Le programme de la question 12 est mal écrit, certaines conditions sont redondantes, et il ne prend pas en compte tous les cas de figure. (égalité ect).
Réécrire le programme de la question 12 qui renvoie la plus grande valeur et son nom de variable. En cas d'égalité, afficher une des deux variables égales.


**Programme 2:**
Récrire le programme du calcul du pain, mais désormais l'utilisateur devra saisir le nombre de pains acheté ainsi que le type de pain.

_Astuce vous pouvez afficher un choix multiple à l'utilisateur en proposant une saisie précise :_

_1.Pour une baguette taper 1_
_2.Pour des croissants taper 2..._


**Programme 3:**
Écrire un programme qui dit si le nombre saisi au clavier est paire ou impaire

**Programme 4:**
Écrire un programme qui calcule et renvoie l'interprétation d’un IMC (google it).
Votre programme prendrait en entrée une taille et un poids (attention aux unités) et renverra une phrase contenant l'IMC et son interprétation.
