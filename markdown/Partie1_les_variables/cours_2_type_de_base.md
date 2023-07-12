# Chapitre 2: Les types de données

Vous avez vu dans le chapitre précedents comment manipuler une variable.Mais nous avons omis un détails important: le type de cette variable.
Un type de donnée définie l'ensembles des valeurs possibles pour les données qu'il admet.On distingue les types de bases décrits dans ce chapitre,
et les types structurés que nous aborderons plus tard dans un autre chapitre.

## les différents type:
python distingue 4 types de données primitifs:
+ nombre:
  - entier
  - virgule
+ chaine de caractères
+ les booléens


### Nombres:
Les types numériques se divisent en deux catégories dans Python : les entiers (Integers) et les virgules flottantes (Floats).

Les nombre entiers (integers, abrégé int) s'ecrive de façon usuelle:
```
10,254,-5
```
ici rien de bien compliqué

Les nombres à virgules flottante (float): il s'agit des nombres décimals:
```
1.254 0.24562 -452.6578
```

/!\ en anglais les décimals sont séparer avec un . et non ,
il en est de même en informatique


0 et 0.0 sont deux type différents

### Les chaines de caractères
il s'agit de textes (string en anglais) encadrée par des guillemets (simple ou double): "ceci est une chaine de caractères".
L'utilisation du type du guillemets permet simplement d'inclure l'autre type de guillemets:
```
"guillmet double m'entours je peut mettre des 'simple' dans mon texte "
'guillmet simple, je peut mettre des "guillmets" dans mon texte'
```

Une chaine de caractere doit tenir sur une seule ligne.Sinon un text doit être délimité par trois guillemets
```
"""
mon texte
sur plusieur ligne
"""
```

### booléens
le dernier type est tres simple, il ne peut prendre que deux valeur: vrai ou faux
noté ``` True ``` et ``` False ```. Elle est utile notamment dans la prise de décision



### afficher le type d'une variable
En python il existe une fonction simple pour afficher le type d'une variable: ``` type(maVariable) ```

```python runnable
A = 10
print(type(A))
B="kezako"
print(type(B))
```


### Note sur les types et le langage python

En python il est inutile de définir à l'avance le type de la variable.C'est l'interpréteur qui le fait tout seule.
Ainsi lorsque on affecte un int à une variable, python sait qu'il s'agit d'un int et on dit que la variable est de type int.
Si on change de type plus tard (en affectant un autre type à la variable), l'interpréteur s'adaptera automatiquement et de maniere transparente pour le développeur.
C'est bien pratique, en python il n'y à donc pas besoin de s'occuper du type de ma variable, puisque l'interpréteur s'occupe de tout.
Oui c'est vrai. Mais il existe des situations ou nous avons besoin que ma variable soit d'un type précis, ou bien de convertir une variable d'un type à une autre.

### conversion des variables
Pour les types de base l'opération est simple.

Convertir une chaine de caractére en entier:int
j'ai extrait la valeur "10" d'une chaine de caractere. Mais python considére toujours que Variable = "10" est une chaine de caractere, or je voudrait l'interpréter entant qu'entier:
variable = int(variable)
variable est désormais du type int
l'opération inverse:
variable = str(variable)
variable est redevenu de type chaine de caractére

Attention à convertir ce qui est convertible! int("abc") renveras une erreur.

Faite des essaie ici:
```python runnable
A = 10
print(type(A))
B = str(A)
print(type(B))
```
