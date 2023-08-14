# Les fonctions

Nous voici dans la derniere partie de ce chapitre sur les bases de la programmation python.
Apres cela vous connaitré toutes les bases pour commencé à écrire des vrai programme informatique!
Cette partie est essentielle à la bonne maitrise du python. Il est impossible d'écrire un programme sans utiliser des fonctions,


**Un peu d'histoire**
Avec ce chapitre on démarre l'écriture d'algorithmes. le mot "algorithme" vient du nom d'un mathématicien arabe du VIII siécle, AL-khwarizmi.Ce mathématicien écrivit en langue arabe le plus ancien traité d'algèbre "am-jabr" sur la résolution des équations.Il y proposait les solutions en décrivant l'enchainement d'étapes à suivre pour résoudre les équations.


## Utilité d'une fonctions
l'ecriture d'une fonction  rend un programme plus simple à comprendre,plus facile à vrifie et plus simple à modifier.
Vous avez déjà utiliser certaine fonction préprogrammées sans le savoir: print(); input(), randint()...
Les fonctions font partie des routines. Ce sont des portions de programme auxquelles on a donné un nom, afin de pouvoir les utiliser ensuite en rappelant juste ce nom.
Une chose à retenir, la redondence du code est l'enemie numéro un du programmeur! Il faut à tout prit évité d'écrire plusieurs fois le même code dans son programme!
Vous découvrirez assez vite les raisons avec l'éxperience.Mais multipilier le même code complique la maintenance et accroit fortement le risque d'érreur!
Sans oublié que cela fait plus de boulot car plus de code à écrire ^^
Revenons à l'utilité des fonctions.
Une fonction est utilisée comme une boite noire: On fournit des valeurs et on récupère "quelque chose".C'est tres pratique lorsque on utlise du code qui n'est pas le notre.

```python
valeur=randint(1,5)
```
Ici je fournit deux valeur à ma fonction: 1 et 5 et la fonction me renvoie un nombre aléatoire dans cette interval. C'est magique, et je n'ai pas le moindre idée de ce qu'il se trouve dans la fonction randint. J'ai juste besoin de connaitre ces paramétre d'entrée et de sortie!

## Définir une fonction
 une fonction est définie par un nom, éventuellement des parametre d'entrée (pas obligatoire), et une sortie (pas obligatoire non plus) puis en donnant le code de cette fonction (bloc)

**Déclaration d'une fonction**
```python
def ma_Fonction(param1,param2):
  #contenu de ma fonction
  return valeurSortie
```

La déclartaion de fonction suit une syntaxe particuliere en python.
Elle commence par le mot clé **def** suivie du nom de la fonction.
Le nommage d'une fonction suit les mêmes restrictions que ceux des variables (alphanumérique,pas de caractere spéciaux...)
puis entre parenthèses une liste de paramètre d'entrée suivie de **:**
Le contenue de ma fonction (bloc d'instruction) doit être indentées
Enfin une fonction peut renvoyé une valeur. On parle alors de valeur de sortie
pour cela on utilise le mot clé **return** suivie de la valeur de sortie.
Attention l'instruction return stop l'execution de la fonction la suite de la fonction ne sera donc pas exécuter.



```python
def addition(val1,val2):
  somme = val1 + val2
  return somme
```
_exemple de fonction_

_ne crée par des fonctions possédant le même nom qu'une de vos variables déjà existant sous peine d'obtenir des résultats aberrants,car l'ordinateur risque de confondre les deux_


**Utiliser une fonction**

L'utilisation d'une fonction est très simple, vous l'avez déjà fait: il suffit d'utiliser sont nom avec ces paramètre:
```python
somme =  addition(10,12)
print("message")
valeur = input()
```

## arguments d'une fonction
Une fonction peut comporter plusieurs arguments (appelés aussi paramètre). Il suffit de séparer par une virgule les différents arguments

```python
def fonctionSansArgument():
  return 10

def fonctionAvecUnArgument(param1):
  return param1+10

def fonctionAvecPlusieurArgument(v1,v2,v3,v4):
  return v1+v2+v3+v4    
```

Un argument de fonction permet d'utiliser des "élements" du programme extérieurs
Le contenu d'une fonction appeler corps de la fonction se situe dans un environnement un peu particulier.Celui-ci contient les valeurs des variables définit hors de la fonction,
mais ne peut pas les modifiers.
_plus tard on verra que ce n'est pas complétement vrai, mais pour l'instant je prefere que vous reteniez ceci,la manipulation de vos variable non pas d'impacte en dehors de votre fonction_

on utilise alors le terme de **variable local** et **variable global**

Reprenons notre toutes premiere analogie de l'étagère de rangement.
Lorsque nous écrivons du code dans une fonction nous nous situons dans une autre chambre avec **exactement** la même étagère possédant les mêmes objet, ranger dans le même ordre.
On parle ici de variable global. Global car elles sont accessible dans tout le programme (y comprit dans les autres chambres).
mais attention ce ne sont pas les même objets, ce sont des sortes de copies!Vous est dans une autre chambre et Si vous modifier le contenue d'une case dans votre nouvelle chambre, cela n'affectera pas la chambre principal.

```python runnable
variableGlobal = 10

def ma_fonction():
  variableGlobal = 20
  print(variableGlobal)

ma_fonction()
print(variableGlobal)
```
Si vous executer le code ci dessus vous voyez bien que la variableGlobal posséde la valeur 20 dans la fonction _ma_fonction_  mais garde la valeur 10 en dehors.

Si dans votre nouvelle chambre vous décidez de rajouter des objets (variable) on parle alors de **variable local** car elle est local à votre nouvelle chambre uniquement.
L'étagere de votre chambre principal n'est pas modifier et ne posséde pas ce nouvelle objet.


```python
def ma_fonction():
  variableLocal = 20

ma_fonction()
print(variableLocal)
```
_l'execution du code ci-dessus renverra une erreur : variableLocal n'est pas définie et n'existe pas_

Mais alors comment je fait si je souhaite modifier la valeur de mes variables global?
Pour cela il existe deux solutions:

Une qui ne faut pas utiliser!!!!!
le mot clés **global**
Je vous explique le fonctionnement mais je vous déconseille tres fortement de l'utiliser car c'est généralement synonime de mauvaise architecture logiciel!

```python runnable
valeurGlobal = 10
def ma_fonction():
  global valeurGlobal
  valeurGlobal = 20

print(valeurGlobal)  
```

L'utilisation du mot clés global permet d'indiquée à l'ordinateur que on fait référence à la valeur original et non une copie.Dans notre analogie, c'est comme si on prend un objet de
l'étagère original pour la mettre dans l'étagère de notre seconde chambre (c'est ici que l'analogie perd de sont sens, car l'objet en question se retrouve à ce moment Et dans la chambre original Et dans la nouvelle chambre.Une sorte d'objet quantic)

Je ne détaillerai pas plus ceci.

La seconde méthode et donc la bonne méthode:
Le parametre de sortie!!!

Si je souhaite modifier une variable global, je peut simplement la réaffecter à la valeur de sortie de mon programme!
```python
valeurGlobal = 10
def ma_fonction(v1):
  v1 +=10
  return v1
valeurGlobal = ma_fonction(valeurGlobal)
```

L'instruction return permet de sortir de ma fonction et de renvoyé une valeur. Cette valeur peut tres bien être la valeur d'une variable local.
C'est un peu comme si on rapportait de notre nouvelle étagère un objet à stocker dans notre étagère principal!



## Point important à propos des fonctions:

**respecter la syntaxe**
Il est impératif de bien respecter la syntaxe de déclaration:
mot clés **def** ne pas oublier **:**
et faire attention à l'indentation!!
Car c'est l'indentation qui indique la fin de notre fonctions
```python
def ma_fonction():
  #je suis dans ma fonctions
  #toujours
  return 0
  #je suis encore dans ma fonctions
print("out") #fin de l'indentation je ne suis plus dans ma fonction
```

**Respecter l'ordre et le type des arguments d'entrée!**
Lorsque on appel une fonction, il est impératif de passer les arguments dans le bonne ordre!
ainsi que le type attendu!

```python
def ma_fonction(param1,param2):
  for i in range(param1):
    print("bonjour je suis " + param2)
```

l'appel ma_fonction("remi",10) ne fonctionnera pas alors que ma_fonction(10,"remi") sera bon

**return permet une sortie de fonction**
une fonction peut contenir plusieur return (notamment dans le cas de test if).Cependant dès qu'une instruction _return_ est exécutée, les lignes suivantes ne sont plus lues.
```python
def ma_fonction(val1):
  if (val1%2)==2:
    return "pair"
  else:
    return "impaire"
  return "ceci est un return jamais lu"  
```
