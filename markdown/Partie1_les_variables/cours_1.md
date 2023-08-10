Ce cours corréspond au chapitre 2 de votre manuel scolaire.
Je vous encourage donc à lire les pages 30 à 38 en paraléle de ce cours, car celui-ci représente un bon complément.
Certaine notions sont expliqué différament dans le manuel que dans le cours ci-dessous et vous conviendra peut être mieux.

# Les variables

Peu importe le langage de programmation utilisé, il existe un point commun entre eux: l'utilisation de variable!

### Commençons par une analogie
Vous venez d'emménager dans votre nouvelle maison,et souhaitez avoir une chambre parfaitement rangée (le rêve de tout parent).
Pour cela vous avez acheté une superbe étagère à casier!! Dans chaque casier vous allez pouvoir y ranger des affaires.

![etagere](../../img/etagere.jpeg)
<div class="alert alert-block alert-info">
  C'est normal que touts les casiers ne soient pas de la même taille?
  Oui, car toutes les affaires ne sont pas de la même taille. Mais on y reviendra plus tard
</div>


Comme vous est quelqu'un d'extrêmement organiser, vous aller étiqueter chaque casier pour que l'on sache ce qu'il y a dedans.

![etagere](../../img/etagere_etiquette.jpeg)

Une **variable** en informatique est un peu comme une casier de notre étagère.
Elle nous permet de stocker une donnée et d'y attribuer une étiquette.

En python elle se déclare ainsi:

```python
Ma_variable = 10
#Attention de ne pas confondre = et == l'opérateur de comparaison
```
<div class="alert alert-block alert-info">
En informatique nous utilisons les termes "déclarer" une variable pour dire que nous avons **crée** une variable.
</div>


 #### Analysons un peu plus en détail cette déclaration:

 Ma ligne de code commence par Ma_Variable. Il s'agit du label (dans notre analogie il s'agit de l'étiquette).
 S'est le nom que nous utiliseront dans la suite du programme pour faire référence au contenu de notre casier.

 <div class="alert alert-block alert-warning">
La casse (le fait de mettre des minuscules et des majuscules) est extrêmement importante. <i> MaVariable </i> est different de <i>mavariable</i>

 </div>


Maintenant analysons la partie droite: la valeur 10.
Il s'agit simplement de la valeur que nous allons affecter à notre variable (dans notre analogie il s'agit des affaires que nous mettons dans notre casier).

Désormais lorsque je souhaite utiliser la valeur 10 dans mon programme je peux utiliser ma variable : Ma_variable

<div class="alert alert-block alert-warning">
Ce n’est pas hyperpratique, pourquoi ne pas simplement utiliser directement la valeur 10 plutôt qu'une variable?
</div>
Pour l'instant et pour cette exemple c'est pas faux. Mais très vite nous allons voire l'utiliter de labeliser des valeurs.

#### Déclaration multiple
Déclarer des variables est quelques chose de très fréquent dans un programme. C'est pourquoi en python il existe différentes syntaxe pour gagner du temps.

```python
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
Dans cet exemple nous nous sommes contentés de modifier le contenu de notre variable A. Nous avons donc retiré de notre casier la valeur 10 pour y stocker la valeur 20 (nous avons simplement remplacé le contenu d'un casier sans modifier son étiquette. C’est comme remplacer une casquette par une autre).

```python runnable
A = 10
A = A*2
print(A)
```
Ici c'est un poil plus complexe: Nous avons modifié le contenu de notre variable A avec la valeur de la variable A!!
Détaillons ce que va faire l'ordinateur exactement:
L'ordinateur va lire la première instruction <i>A = </i> (il comprend donc qu'il va devoir modifier la valeur présente dans le casier, mais pour l'instant il ne fait rien).
Ensuite il analyse ``` A*2 ``` autrement dit ``` valeur du casier A * 2 ``` a cette étape le contenu du casier A n'a pas encore été modifié, il vos donc toujours ```10```. L’ordinateur remplace donc
L’instruction ```A*2```  par ```10*2``` , ce qui donnera l'instruction une fois analyser ```A = 20```


<div class="alert alert-block alert-warning">
Modifier une variable est une chose très fréquente. Notamment l'incrémentation d'un indice, c'est pourquoi il existe une syntaxe un peu plus rapide:
```python
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


## Les opérateurs:
On manipule les valeurs et les variables qui les référencent, en les combinant avec des opérateurs pour former des expressions. Exemple :
```python
a, b = 7.3, 12
y = 3*a + b/5  
```

Dans cet exemple, nous commençons par affecter aux variables a et b les valeurs 7,3 et 12. Comme déjà expliqué précédemment, Python assigne automatiquement le type « réel » à la variable a, et le type « entier » à la variable b.

La seconde ligne de l'exemple consiste à affecter à une nouvelle variable y le résultat d'une expression qui combine les opérateurs *** , +** et **/** avec les opérandes a, b, 3 et 5. Les opérateurs sont les symboles spéciaux utilisés pour représenter des opérations mathématiques simples, telles l'addition ou la multiplication. Les opérandes sont les valeurs combinées à l'aide des opérateurs.


Python évalue chaque expression qu'on lui soumet, aussi compliquée soit-elle, et le résultat de cette évaluation est toujours lui-même une valeur. A cette valeur, il attribue automatiquement un type, lequel dépend de ce qu'il y a dans l'expression. Dans l'exemple ci-dessus, y sera du type réel, parce que l'expression évaluée pour déterminer sa valeur contient elle-même au moins un réel.

On peut donc calculer des formules mathématiques avec les opération arithémtiques usuelles: addition **+** soustraction **-** multiplication **\*** et division **/**

Les opérateurs Python ne sont pas seulement les quatres opérateurs mathématiques de base. Il faut leur ajouter l'opérateur **\*\*** pour l'exponentiation, ainsi qu'un certain nombre d'opérateurs logiques, des opérateurs agissant sur les chaînes de caractères, des opérateurs effectuant des tests d'identité ou d'appartenance, etc. Nous reparlerons de tout cela plus loin.Mais voici quelques un utile à retenir:
**//** pour la division entiere et **%** pour le reste (dit modulo)


### Pratiquons un peu

@[Okay! entraine toi!]({"stubs": ["./les_variables/ex1.py"], "command": "python3 ./les_variables/valide_ex1.py"})


### A savoir
Maintenant que nous savons ce qu'est une variable et comment la manipuler, il est temps de faire un petit point sur la syntaxe de ces variables.
J'ai dit qu'on pouvait labelliser notre variable avec le nom que l’on veut. Ce n'est pas tout à fait vrai. Il existe quelque petite restriction:
> +Seuls les caractères alphanumériques (a-z,A-Z, et 0-9) sont autorisés ainsi que l'underscore
> + Le nom d'une variable ne doit pas commencer par un chiffre
> + Pas d'espace dans les variables (peut être contourné avec _)
> + Ils sont sensibles à la casse
> + Certains noms sont réservés aux fonctions système:For,while,def,int,float... (vous les découvrirez au fur et à mesure de votre apprentissage python)


<div class="alert alert-blocl alert-info">
  Nommez une variable de manière la plus claire et descriptive possible façilitera grandement la lisibilité de votre code.
  Certains langage impose des conventions de nommage. Ce n'est pas le cas de python, cependant il vous est grandement conseillers d'en avoir.
  Cela facilite la compréhension du code.
</div>
