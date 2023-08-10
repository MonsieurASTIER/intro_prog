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
Ecrire sur votre IDE les différents programmes:

**programme 1:**

1. Ecrire une boucle bornée (For) qui affiche les nombres pairs entre 2 et 20
2. Ecrire une boucle non bornée(while) qui fasse la même choses
3. Même question pour afficher les nombre paire entre 20 et 2 par ordre décroissant.

**Programme 2:**

Ecrire un programme qui affiche les 10 premiers nombre de la suite de fibonnachi (google it)

**programme 3:**

Ecrire un programme qui affiche le nombre de seconde qui reste avant la fin de la journée.
L'heure sera définie par un flottant dont la partie entiere définira les heures, et la partie décimales les minutes. ainsi 8.15 correspond à 8h15
Tester votre programmes avec les variables:
```
heure_1 = 12.00
heure_2 = 14.30
heure_3 = 0.0
heure_4 = 23.12   
```

**programme 4:**
Soit la suite mathé
matique u0 = 0 et Un+1 = 2Un
Ecrire un programme qui renvoie la valeur de U10


**programme 5:**
1. Ecrire un programme qui indique si une année est bissextile.Une année est bissextile si elle est divisible par 4.cependant les siécles ne sont pas bissextiles sauf
les multiples de 400.
2. Compléter le programme pour calculer le nombre de jours du mois m, m étant un entier compris entre 1 et 12.De janvier à juillet les mois impaires ont 31 jours,les autres 30.de Aout à décembre c'est l'inverse.
De pus le mois de février à 29 ou 28jours selon que léannée est bissextile ou non.

**programmes 6:**

1. Ecrire un programme qui étant donnée un nombre entre 2 et 12 affiche toutes les combinaisons possibles permettant d'obtenir ce nombre avec deux dés.
2. Étendre le programme ci dessus pour afficher,pour chaque nombre entre 2 et 12,toutes les combinaisons possibles permettant d'obtenir ce nombre avec deux dés.
3. Modifier le programme pour afficher seulement le nombre de combinaisons possibles pour chaque total, au lieu des combinaisons elles-mêmes

**programme 7**

On veut calculer la monnaie à rendre sur un paiement en euros(sans les cents).
La monnaie est rendue avec des pieces et des billets de 1€ ,2€ 5€ 10€ et 50€
1. Ecrire un programme qui calcule et affiche le nmbre de piece et billets de chaque valeur à rendre
pour les variables
prix=42
paiement=50

tester votre programme avec différentes valeurs de variables.

2. maintenant le contenu de la caisse est représenté par un ensemble de variable correspondant au nombre de pièces et de billets de chaque valeur:
```python
  nb_1_euros = 15 #nombre de piece de 1euros present dans la caisses
  nb_2_euros = 4
  nb_10_euros = 12
  nb_20_euros = 5
  nb_50_euros = 4
```
adapter le programme précédents pour afficher la monnaie à rendre en fonction du contenu de la caisse et mettre à jours la caisse.
