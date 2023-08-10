# Pratiquons un peu


Bon, il est temps de passer à la pratique.
Avant de commencer, voici quelques instructions qui vont vous être utiles dans votre vie de développeur Python:


## Afficher du texte dans un terminal

La plupart de vos premiers programmes ne disposeront pas d'interface graphique, mais simplement un terminal (ou console).
Pour afficher du texte dans la console, il existe une fonction simple : print()


```python
#Afficher un texte
print("Ce que je souhaite afficher")

#Afficher le contenu d'une variable
variableA = 10
print(variableA)
```



## Commenter votre code

On y reviendra plus tard, mais il est **très important** de commenter vos codes.
C'est-à-dire de rajouter des commentaires qui ne seront pas lus par l'ordinateur, mais simplement pour les autres développeurs
Ceci se fait avec le caractère **#**

```python
# ceci n'est pas interpréter par l'ordinateur
```

Tout ce qui suit un # n'est pas lu par l'ordinateur (un peu comme si la ligne n'existait pas)


## Récupérer une saisie clavier

Une dernière fonction qui vous sera utile : input()
Cette fonction permet de récupérer une saisie clavier

```python
A = input() #si utilisateur saisie "abc" alors la variable A="abc"
```

Il est possible de rajouter un affichage à votre commande input("afficher le message")

```python
print("Message affiché")
A = input()
# est équivalant à
A = input("Message affiché")
```

/!\ input renvoie un type str (chaîne de caractère).

_Si vous n'avez pas compris cette phrase, relisez la partie sur les types de bases_


# À vous de jouer :

À l'aide de votre environnement de développement, écrire les programmes suivants :

**Programme 1:**

Écrire l'expression qui calcule la moyenne de deux nombres A et B
Afficher la moyenne pour la valeur A = 12 et B = 8


**Programme 2:**

Écrire l'expression qui calcule la réduction d'un produit soldé
Afficher la valeur de la réduction pour un objet coûtant 50€ et une réduction de 10%
Exemple : un couteau à 80€ solder à 20% donne une réduction de 16€

**Programme 3:**

À l'aide de l'instruction input(), écrire un programme qui calcule le coût de votre commande de pain
Sachant que le prix d'une baguette est de 1.20€ et le nombre de baguettes acheté dépendra de votre saisie clavier
Le programme devra donc demander à l'utilisateur combien de baguette, il souhaite acheter.

**Programme 4:**
1. Trouver les valeurs suivantes, par exemple dans Wikipédia et écrire les valeurs python correspondant (attention aux unités)

+ Distance **d** de la terre au soleil
+ Vitesse **C** de la lumière
+ Circonférence **t** de la terre
+ Population **P** de la terre

2.À partir des valeurs précédentes, écrire les expressions qui calculent les valeurs suivantes (attention aux unités !)

+ Temps mis par la lumière du soleil pour atteindre la terre
+ Vitesse moyenne de la terre autour du Soleil, en supposant que la trajectoire soit circulaire
+ Nombre de fois qu'un signal électrique fait le tour de la terre en 1 seconde
+ Surface de la terre
+ Densité moyenne de la Population de la terre, sachant que 70,7% de la surface de la terre est immergée

Afficher les différentes réponses de manière lisible dans la console (Exemple : "La lumière met x seconde pour atteindre la terre depuis le soleil.")

**Programme 5:**

Dans le bourgeois Gentilhomme, le maître de philosophie dit :
On les peut mettre premièrement comme vous avez dit : "Belle marquise, vos beaux yeux me font mourir d'amour."
ou bien "D'amour mourir me font, belle Marquise, vos beaux yeux"
ou encore : "Vos yeux beaux d'amour me font, belle marquise,mourir."
ou "Mourir, vos beaux yeux, belle marquise, d'amour me font"
pour finir, "Me font vos yeux beaux mourir, belle marquise, d'amour"
Définir différentes variables contenant les morceaux de la phrase "belle marquise...", de telle sorte que l'on
puisse afficher, avec la fonction print et l'opérateur + des chaînes de caractère correspondant aux différentes variantes énoncées. (on ignore la case)
Afficher ces différentes variantes
