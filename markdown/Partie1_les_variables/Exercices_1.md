# Pratiquons un peu

Bon il est temps de passer à la pratique.

Avant de commencer voici quelques instruction qui vont vous être utile dans votre vie de développeur python:

## Afficher des trucs dans un terminal
La plupart de vos 1er programme ne disposeront pas d'interface graphique, mais simplement un terminal ( ou console).
Pour cela il existe une fonction simple:

```
#Afficher un texte
print("Ce que je souhaite afficher")

#Afficher le contenue d'une variable
variableA = 10
print(variableA)
```

## Commenter votre code
On y reviendra plus tard, mais il est **tres important** de commenté vos code.
C'est à dire de rajouter des commentaires qui ne seront pas lu par l'ordinateur mais simplement pour les autres développeur
Ceci se fait avec le caractére #

```
 #ceci n'est pas interpréter par l'ordinateur
```  

Tout ce qui suit un # n'est pas lu par l'ordinateur (un peu comme si la ligne n'existait pas)


## Récuperer une saisie clavier
Une dernier instruction qui vous sera utile: input()
Cette instruction permet de récuperer une saisie clavier

```
A = input()
#si utilisateur saisie "abc" alors la variable A="abc"
```

Il est possible de rajouter un affichage à votre commande input("afficher le message")

```
print("message afficher")
A = input()
# est équivalant à

A = input("message afficher")
```

/!\ input renvoie un type str (chaine de caractére)
Si vous n'avez pas comprit cette phrase relisé la partie sur les types de bases


# A vous de jouer:

A l'aide de votre environnement de développement écrire les programmes suivants:


**Programme 1:**
  Ecrire l'expression qui calcule la moyenne de deux nombre A et B
  Afficher la moyenne pour la valeur A = 12 et B = 8

**Programme 2:**
  Ecrire l'expression qui calcule la reduction d'un produit solder
  Afficher la valeur de la réduction pour un objet coutant 50€ et une reduction de 10%
  exemple: Un couteaux à 80€ solder à 20% donne une réduction de 16€


**Programme 3:**
  À l'aide de l'instruction input(), écrire un programme qui calcule le couts de votre commande de pain
  Sachant que le prix d'une baguette est de 1.20€ et le nombre de baguette acheté dépendra de votre saisie clavier
  Le programme devra donc demander à l'utilisateur combien de baguette il souhaite acheter

**Programme 4:**
  **A.** Trouver les valeurs suivantes,par exemple dans wikipedia et ecrire les valeurs python correspondante (attention au unité)
  + Distance **d** de la terre au soleil
  + Vitesse **C** de la lumière
  + Circonférence **t** de la terre
  + Population **P** de la terre
  **B.** À partir des valeurs précédentes, ecrire les expressions qui calculent les valeurs suivantes (attention au unités!)
  + Temps mis par la lumière du soleil pour atteindre la terre
  + Vitesse moyenne de la terre autour du Soleil, en supposant que la trajectoire est circulaire
  + Nombre de fois qu'un signal électrique fait le tour de la terre en 1seconde
  + Surface de la terre
  + Densité moyenne de la Population de la terre, sachant que 70,7% de la surface de la terre est immergée

  afficher les différentes réponses de manière lisible dans la console (exemple: "La lumière mets x seconde pour atteindre la terre depuis le soleil")

**Programme 5:**
  Dans le bourgeois Gentilhomme, le maitre de philosophie dit:
  On les peut mettre premièrement comme vous avez dit: "Belle marquise, vos  beaux yeux me font mourrir d'amour"
  ou bien "D'amour mourir me font, belle Marquise, vos beaux yeux"
  ou encore: "Vos yeux beaux d'amour me font, belle marquise,mourrir"
  ou "Mourrir vos beaux yeux, belle marquise, d'amour me font"
  pour finir "Me font vos yeux beaux mourir, velle marquise, d'amour"

  Definir différente variable contenant les morceaux de la phrases "belle marquise...", de telle sorte que l'on
  puisse afficer avec la fonction print et l'opérateur + des chaines de caractére corrépondant au différentes variantes énoncées. (on ignoe la case)
  Afficher ces différentes variantes



Exercice fonction:
Ecrire une fonction qui renvoie la réduction des soldes
@IN: PRIX
@IN: Reduction en pourcent
@OUT: PRIX final (une fois la reduction appliquer)
