#Chapitre 2: Les types de données

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
noté True et False. Elle est utile notamment dans la prise de décision


python:afficher le type d'une variable


En python il est inutile de définir à l'avance le type de la variable.C'est l'interpréteur qui le fait tout seule.
Ainsi lorsque on affecte un int à une variable, python sait qu'il s'agit d'un int et on dit que la variable est de type int.
Si on change de type plus tard (en affectant un autre type à la variable), l'interpréteur s'adaptera automatiquement et de maniere transparente pour le développeur.
Nous verons un peu plus tard les conséquences du changement de type
