# Les types de données

Vous avez vu dans la partie précédente comment manipuler une variable. Mais nous avons omis un détail important : le type de cette variable.
Un type de donnée, définie l'ensemble des valeurs possibles pour les données qu'il admet.
On distingue les types de bases décrits dans ce chapitre,
et les types structurés que nous aborderons plus tard dans un autre chapitre.

## les différents type:
python distingue 4 types de données primitifs:
+ Nombre
- Entier
- Virgule
+ Chaine de caractères
+ Booléens

## Nombres:
Les types numériques se divisent en deux catégories dans Python : les entiers (Integers) et les virgules flottantes (Floats).

Les nombres entiers (integers, abrégé int) s'écrivent de façon usuelle:
```
10,254,-5
```
ici rien de bien compliqué

Les nombres à virgule flottante (float): il s'agit des nombres décimaux:
```
1.254 0.24562 -452.6578
```

/!\ en anglais les décimales sont séparées avec un. et non,
Il en est de même en informatique


0 et 0.0 sont donc deux types différents.



## Les chaînes de caractères (str)
Il s'agit de texte (appelé string en anglais) encadrés par des guillemets (simples ou doubles): "ceci est une chaîne de caractères".
L'utilisation du type du guillemet permet simplement d'inclure l'autre type de guillemets :
```
"guillemet double m'entours je peux mettre des 'simple' dans mon texte "
'guillemet simple, je peux mettre des "guillemets" dans mon texte'
```

Une chaîne de caractère doit tenir sur une seule ligne. Sinon un texte doit être délimité par trois guillemets
```
"""
mon texte
sur plusieur ligne
"""
```



## Les booléens (bool)
Le dernier type est très simple, il ne peut prendre que deux valeurs: vrai ou faux
Noté ``` True ``` et ``` False ```. Elle est utile notamment dans la prise de décision

**Afficher le type d'une variable**
En python il existe une fonction simple pour afficher le type d'une variable: ``` type(maVariable) ```

```python runnable
A = 10
print(type(A))
B="kezako"
print(type(B))
```


### Note sur les types et le langage python

En python, il est inutile de définir à l'avance le type de la variable. C'est l'interpréteur qui le fait tout seul.
Ainsi, lorsque on affecte un int à une variable, Python sait qu'il s'agit d'un int et on dit que la variable est de type int.
Si on change de type plus tard (en affectant un autre type à la variable), l'interpréteur s'adaptera automatiquement et de manière transparente pour le développeur.
C'est bien pratique, il n'y a donc pas besoin de s'occuper des types, l'interpréteur s'occupe de tout !
Oui c'est vrai, mais il existe des situations où nous avons besoin que nos variables soient d'un type précis, ou bien de convertir une variable d'un type à une autre.

Exemple:
```python
variableString = "ma chaine 10"
valeurExtraite = variableString[-2:] #ici j'extrait les 2 dernier caractere de la chaine: 10
```
La variable _valeurExtraite_ vaut désormais la chaîne de caractère: "10"
Que faire si je veux interpréter cette valeur comme le nombre 10 et non la chaîne de caractère "10"?

### conversion des variables
Pour les types de base, l'opération est simple.
Convertir une chaîne de caractère en entier : **int**
> ```variable = int(variable)```
variable est désormais du type int

l'opération inverse **str**:

>```variable = str(variable)```
variable est redevenu de type chaîne de caractère.

Attention à convertir ce qui est convertible ! ```int("abc")``` renverra une erreur.
Faites des essais ici :

```python runnable
A = 10
print(type(A))
B = str(A)
print(type(B))
```
