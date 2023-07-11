# Les variables

Peu importe le langage de programmation utilisé, il existe un point commun entre eux: l'utilisation de variable!

### Commençons par une analogie
Vous venez d'emménager dans votre nouvelle maison,et souhaitez avoir une chambre parfaitement rangée (le rêve de tout parent).
Pour cela vous avez acheté une superbe étagère à case!! Dans chaque case vous allez pouvoir y ranger des affaires.

![etagere](../../img/etagere.jpeg)
<div class="alert alert-block alert-info">
  C'est normal que toutes les cases ne soient pas de la même taille?
  Oui, car toutes les affaires ne sont pas de la même taille. Mais on y reviendra plus tard
</div>


Comme vous est quelqu'un d'extrêmement organiser, vous aller étiqueter chaque case pour que l'on sache ce qu'il y a dedans.

![etagere](../../img/etagere_etiquette.jpeg)

Une **variable** en informatique est un peu comme une case de notre étagère.
Elle nous permet de stocker une donnée et d'y attribuer une étiquette.

En python elle se déclare ainsi:

```
Ma_variable = 10
#Attention de ne pas confondre = et == l'opérateur de comparaison
```
<div class="alert alert-block alert-info">
En informatique nous utilisons les termes "déclarer" une variable pour dire que nous avons **crée** une variable.
</div>


 #### Analysons un peu plus en détail cette déclaration:

 Ma ligne de code commence par Ma_Variable. Il s'agit du label (dans notre analogie il s'agit de l'étiquette).
 S'est le nom que nous utiliseront dans la suite du programme pour faire référence au contenu de notre case.

 <div class="alert alert-block alert-warning">
La casse (le fait de mettre des minuscules et des majuscules) est extrêmement importante. <i> MaVariable </i> est different de <i>mavariable</i>

 </div>


Maintenant analysons la partie droite: la valeur 10.
Il s'agit simplement de la valeur que nous allons affecter à notre variable (dans notre analogie il s'agit des affaires que nous mettons dans notre case).

Désormais lorsque je souhaite utiliser la valeur 10 dans mon programme je peux utiliser ma variable : Ma_variable

<div class="alert alert-block alert-warning">
Ce n’est pas hyperpratique, pourquoi ne pas simplement utiliser directement la valeur 10 plutôt qu'une variable?
</div>
Pour l'instant et pour cette exemple c'est pas faux. Mais très vite nous allons voire l'utiliter de labeliser des valeurs.

#### Déclaration multiple
Déclarer des variables est quelques chose de très fréquent dans un programme. C'est pourquoi en python il existe différentes syntaxe pour gagner du temps.

```
A = 10
B = 4
C = 25600
```
Peut s’écrire plus rapidement:

```python runnable
A,B,C = 10,4,25600
print(A)
print(B)
print(C)
```

/!\ Dans ce cas , faite attention de ne pas vous tromper dans l'ordre de Déclaration

A,B,C = 10,4,25600 sera différent de A,C,B = 10,4,25600


### Modifier le contenue d'une variable
Bon il est temps de rentré dans le vif du sujet. L'interet majeur de déclarer une variable est de pouvoir y modifier sont contenue.
Il est effectivement possible de modifier le contenu d'une variable déjà déclarer.

```python runnable
A = 10
A = 20
print(A)
```
Dans cet exemple nous nous sommes contentés de modifier le contenu de notre variable A. Nous avons donc retiré de notre case la valeur 10 pour y stocker la valeur 20 (nous avons simplement remplacé le contenu d'une case sans modifier son étiquette. C’est comme remplacer une casquette par une autre).

```python runnable
A = 10
A = A*2
print(A)
```
Ici c'est un poil plus complexe: Nous avons modifié le contenu de notre variable A avec la valeur de la variable A!!
Détaillons ce que va faire l'ordinateur exactement:
L'ordinateur va lire la première instruction <i>A = </i> (il comprend donc qu'il va devoir modifier la valeur de la case, mais pour l'instant il ne fait rien).
Ensuite il analyse ``` A*2 ``` autrement dit ``` valeur de la  case A *2 ``` a cette étape la case A n'a pas encore été modifié, elle vos donc toujours ```10```. L’ordinateur remplace donc
L’instruction ```A*2```  par ```10*2``` , ce qui donnera l'instruction une fois analyser ```A = 20```


<div class="alert alert-block alert-warning">
Modifier une variable est une chose très fréquente. Notamment l'incrémentation d'un indice, c'est pourquoi il existe une syntaxe un peu plus rapide:
```
A += 1
#Équivaux à
A = A +1
```

Cette syntaxe est valable pour tous les opérateurs (+-*/)
```python runnable
A = 10
A *=2
print(A)
```
</div>

### Pratiquons un peu

@[Okay! entraine toi!]({"stubs": ["./les_variables/ex1.py"], "command": "python3 ./les_variables/valide_ex1.py"})


### A savoir
Maintenant que nous savons ce qu'est une variable et comment la manipuler, il est temps de faire un petit point sur la syntaxe de ces variables.
J'ai dit qu'on pouvait labelliser notre variable avec le nom que l’on veut. Ce n'est pas tout à fait vrai. Il existe quelque petite restriction:
> Seuls les caractères alphanumériques (a-z,A-Z, et 0-9) sont autorisés ainsi que l'underscore
> Le nom d'une variable ne doit pas commencer par un chiffre
> Pas d'espace dans les variables (peut être contourné avec _)
> Ils sont sensibles à la casse
> Certains noms sont réservés aux fonctions système:For,while,def,int,float... (vous les découvrirez au fur et à mesure de votre apprentissage python)
