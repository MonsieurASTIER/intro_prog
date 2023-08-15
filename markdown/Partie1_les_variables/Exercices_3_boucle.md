# Mise en pratique


```python
for i in range(10):
  print(i*2)
```

?[1. Qu'affiche le programme ci-dessus]
-[] 0,1,2,3,4,5,6,7,8,9
-[X] 0,2,4,6,8,10,12,14,16,18
-[] 0,2,4,8,16,32,64,128,256,512
-[] affiche rien

---
---

```python
a=0
for i in range(10):
  a += i
  print(a)
```

?[2. Qu'affiche le programme ci-dessus]
-[] 0,1,2,3,4,5,6,7,8,9
-[X] 0,1,3,6,10,15,21,28,36,45
-[] 0,2,4,8,16,32,64,128,256,512
-[] affiche rien

---
---

```python
a=0
for i in range(5):
  for j in range(5):
    print(i+j)
```

?[3. Qu'affiche le programme ci-dessus]
-[] 0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4
-[X] 0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7,4,5,6,7,8
-[] 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
-[] affiche rien

---
---

```python
a=0
for i in range(5):
  for j in range(i):
    print(i+j)
```
?[4. Qu'affiche le programme ci-dessus]
-[X] 1,2,3,3,4,5,4,5,6,7
-[] 0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7,4,5,6,7,8
-[] 0,0,1,0,1,2,0,1,2,3,0,1,2,3,4
-[] affiche rien

---
---

```python
a=0
while a < 10:
  a+=1
print(a)
```
?[5. Qu'affiche le programme ci-dessus]
-[] 0,1,2,3,4,5,6,7,8,9
-[] 0,1,2,3,4,5,6,7,8,9,10
-[X] 10
-[] boucle infinie

---
---
```python
a,b = 0,20
while a < b:
  a+=1a,b = 0,0
while a<10:
  b = a +1  
  b-=1
print(a)
```
?[6. Qu'affiche le programme ci-dessus]
-[] 20
-[] 0
-[X] 10
-[] boucle infinie

---
---

```python
a = 0
while 1==1:
  a+=1

print(a)
```
?[7. Qu'affiche le programme ci-dessus]
-[] 20
-[] 0
-[] 10
-[X] boucle infinie

---
---

```python
a,b = 0,0
while a<10:
  b = a +1  
print(a)
```
?[8. Qu'affiche le programme ci-dessus]
-[] 20
-[] 0
-[] 10
-[X] boucle infinie


# Programme:
Écrire sur votre IDE les différents programmes :

**programme 1:**

1. Écrire une boucle bornée (For) qui affiche les nombres pairs entre 2 et 20
2. Écrire une boucle non bornée (while) qui fasse la même chose
3. Même question pour afficher les nombres pairs entre 20 et 2 par ordre décroissant.

**Programme 2:**

Écrire un programme qui affiche les 10 premiers nombres de la suite de fibonnacci (google it)


**programme 3:**
Soit la suite mathématique u0 = 1 et Un+1 = 2Un
Écrire un programme qui renvoie la valeur de U10


**programme 4**
Un joueur doit trouver un nombre entier choisi au préalable de 1 à 100 par l'ordinateur. A chaque tour, le joueur propose un nombre et l'ordinateur peut répondre de trois façons différentes :
Gagné !;  Trop petit; Trop grand

_Pour utiliser de l'aléatoire dans python vous devez utiliser la fonction =randint(0,100) qui renvoie un entier aléatoire entre 0 et 100_
_Pour utiliser cette fonction, vous devez importer sont module (je détaillerai plus tard). Pour cela rajouter au tout début de votre programme l'instruction_
>from random import *

1. Ecrire un programme permettant de jouer à "Devine le nombre".   
2. On veut complexifier le jeu en imposant un nombre d'essais maximal.Modifier le programme précédent afin qu'il...
demande à l'utilisateur de saisir un nombre entier qui corrrespond au nombre maximum d'essais autorisés.permette de jouer sans autoriser plus d'essais que le nombre maximum entré.affiche soit la défaite soit la victoire en précisant le nombre d'essais utilisés.


**Programme 5**
Ecrire un programme qui affiche une a une le code Unicode des caractères du mot "bonjour"
_ord('l')_ renvoie le code unicode du caractere 'l'

**programme 6**
Sur un jeu d'échecs, les cases sont repérées par une lettre (de A jusqu'à H) et par un chiffre (de 1 jusqu'à 8).
Les cases sont donc A1, A2, A3, ..., H7, H8.
Proposer un code qui écrit toutes les cases possibles.

**programme 5:**
1. Écrire un programme qui indique si une année est bissextile. Une année est bissextile si elle est divisible par 4. Cependant, les siècles ne sont pas bissextils sauf
les multiples de 400.
2. Compléter le programme pour calculer le nombre de jours du mois m, m étant un entier compris entre 1 et 12.

De janvier à juillet les mois impaires ont 31 jours, les autres 30.

D'aout à décembre, c'est l'inverse.
De pus le mois de février à 29 ou 28 jours selon que l'année est bissextile ou non.

**programmes 6:**

1. Écrire un programme qui étant donné un nombre entre 2 et 12 affiche toutes les combinaisons possibles permettant d'obtenir ce nombre avec deux dés.
2. Étendre le programme ci-dessus pour afficher, pour chaque nombre entre 2 et 12, toutes les combinaisons possibles permettant d'obtenir ce nombre avec deux dés.
3. Modifier le programme pour afficher seulement le nombre de combinaisons possibles pour chaque total, au lieu des combinaisons elles-mêmes

**programme 7**

On veut calculer la monnaie à rendre sur un paiement en euros (sans les cent).
La monnaie est rendue avec des pièces et des billets de 1€ ,2€ 5€ 10€ et 50€
1. Écrire un programme qui calcule et affiche le nombre de pièces et billets de chaque valeur à rendre
pour les variables
prix=42
paiement=50

Tester votre programme avec différentes valeurs de variables.

2. Maintenant, le contenu de la caisse est représenté par un ensemble de variables correspondant au nombre de pièces et de billets de chaque valeur :
```python
nb_1_euros = 15 #nombre de piece de 1euros present dans la caisses
nb_2_euros = 4
nb_10_euros = 12
nb_20_euros = 5
nb_50_euros = 4
```
Adapter le programme précédent pour afficher la monnaie à rendre en fonction du contenu de la caisse et mettre à jour la caisse.
