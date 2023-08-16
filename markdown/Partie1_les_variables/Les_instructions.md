Avant de commencer cette partie, retournée sur votre google Classroom et effectué les exercice du document sur Algébre de bool:
https://docs.google.com/document/d/1_9rLBXH5yDId6xlZ4UFXkwaO44OCEeLj8_XE7gRqlb4/edit?usp=sharing


Jusqu'à maintenant, nous nous sommes contenté de faire des calculs mathématiques simples, mais nous n'avons pas encore fait d'algorithmie.
Or, pour résoudre un problème informatique, il faut toujours effectuer une série d'actions dans un certain ordre. La description structurée de ces actions et de l'ordre dans lequel il convient de les effectuer s'appelle un algorithme.
Nous allons donc ici apprendre à contrôler le déroulement de votre programme avec des conditions.

# Le déroulement d'un programme

Le déroulement du programme est l’ordre dans lequel les lignes de code sont exécutées. Certaines lignes seront lues une fois seulement, d’autres plusieurs fois. D’autres encore pourraient être complètement ignorées, tout dépend de la façon dont vous les avez codées.

Les instructions conditionnelles sont un moyen de contrôler la logique et le déroulement de votre code avec des conditions.
Elles sont les briques de bases d'un programme, et permettent, en fonction du résultat de l'évaluation d'une expression booléenne, d'exécuter une certaine portion de code plutôt qu'une autre.

## Les instructions conditionnelles

![instruction](../../img/bloc_condition.png)

Vous en avez déjà tous fait sans le savoir. Il s'agit simplement de prendre une décision en fonction de paramètre :
- Si j'ai le temps alors j'irai faire du sport
- Si j'ai des bonnes notes alors j'aurai une SWITCH pour noël
- Si je fais les exercices du cours alors j'arriverai facilement à coder sinon je vais galérer

Toutes ces phrases ont une chose en commun : une instruction conditionnelle **SI**

La conditionnelle est une structure qui permet d'exécuter du code selon qu'une condition est remplie ou non.
Elle s’implémente en python de la forme :


```python
if condition:
  bloc A
```
Le bloc A ne sera exécuté que si la condition est remplie
Analyser bien la syntaxe : la condition commence par l'instruction **IF** suivie de la _condition_ suivie de **:** puis d'un retour à la ligne.
Le bloc commence par une **indentation**.


**Précision importante :**
Python est très sensible à l'indentation (le nombre de caractère espace et retour à la ligne)
Une séquence d'instructions, toutes indentées du même nombre d'espaces, est appelée un bloc. C'est ainsi que le langage python différencie la séquence d'instruction à effectuer quand la condition est remplie.

```python
if condition :
  blocA
  blocA
  blocA
blocB
blocB

```

```python
if condition:
bloc A
```
Ceci renverra une erreur de syntaxe. (_syntax error_ ou _indentationError_) (retenez ces messages d'erreur vous les verrez souvent ;)



```python runnable
if 1+1 == 2 :
  print("La condition est vrai alors j'affiche le message")

if 1+1 > 2 :
  print("c'est faux donc ce message ne s'affichera pas.")
```

**

Nous pouvons rajouter une instruction **else** qui sera exécuté que si la condition **if** n'est pas remplie.

```python
if condition:
  bloc A
else:
  bloc B
```
Dans cet extrait soit le code A sera exécuté, soit le code B **mais jamais les deux**
_else_ se traduit par _sinon_:
Soit j'exécute le bloc A sinon j'exécute le bloc B.

```python runnable
if 1+1 > 2 :
 print("c'est faux donc se message ne s'affichera pas")
else:
 print("du coup, c'est ce message qui s'affiche.")
```

Plusieurs tests peuvent être enchaînés grâce au mot-clé **elif** (qui est l'abréviation de else if)

```python
if condition A:
  bloc A
elif conditionB:
  bloc B
elif conditionC:
  bloc C
else:
  bloc D
```

Attention cependant à l'ordre des elif, car **un seul bloc sera exécuter**: celui de la première condition remplie.
Le compilateur analysera dans l'ordre les différentes conditions (ici condition A puis condition B...) et s'arrêtera dès qu'une condition sera remplie.

## Condition imbriquée :
Ce n'est pas bien compliqué, il s'agit simplement d'une instruction conditionnelle dans une autre instruction conditionnelle :
Voyez plutôt :
```python
if condition A:
  if conditionAA:
    bloc AA
  else:
    bloc AB
else:
  bloc B
```

Ici, le bloc AA sera exécuté si la condition A est remplie et la condition AA.
Si la condition A est remplie, mais pas la condition AA alors le bloc AB sera exécuté.
Si la condition A n'est pas remplie, alors le bloc B est exécuté (la condition AA n'est même pas testée.).



## Retour sur les opérateurs
Il est important de bien comprendre le fonctionnement des opérateurs et des instructions conditionnelles, car cela représente 80% de votre futur travail de développeur.

**Les opérateurs logiques**

| Instruction python | Signification |
| ------ | ----------- |
| a == b | a est égal à b |
| a > b | a est strictement supérieure à b |
| a >= b | a est supérieure ou égale à b |
| a != b | a est différent de b |
| a < b and b > c| a est inférieure à b ET b et supérieure à c |
| a < b or b > c| a est inférieure à b OU b et supérieure à c |
| a < b ^ b > c| a est inférieure à b (OU exclusif) b et supérieure à c |
| not(True) | le contraire de True |

Le **XOR** (ou exclusif) signifie l'un ou l'autre, mais pas les deux

À cela, on peut rajouter quelques opérateurs sur les chaînes de caractère :

| Instruction python | Signification |
| ------ | ----------- |
| "a" == "A" | vaut False |
| "on" in "bon" | Vaut True |
| "on" not in "bon" | Vaut False |


L'opérateur **in** permet de tester l'appartenance d'une chaîne à une autre (si celle-ci est présente dans l'autre)
