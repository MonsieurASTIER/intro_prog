# Les fonctions

Nous voici dans la dernière partie de ce chapitre sur les bases de la programmation python.
Après cela, vous connaîtrez toutes les bases pour commencer à écrire des vrais programmes informatiques !
Cette partie est essentielle à la bonne maîtrise du python. Il est impossible d'écrire un programme sans utiliser des fonctions.


**Un peu d'histoire**

Avec ce chapitre, on démarre l'écriture d'algorithmes. Le mot "algorithme" vient du nom d'un mathématicien arabe du VIII siècle, AL-khwarizmi. Ce mathématicien écrivit en langue arabe le plus ancien traité d'algèbre "am-jabr" sur la résolution des équations. Il y proposait les solutions en décrivant l'enchaînement d'étapes à suivre pour résoudre les équations.

## Utilité d'une fonction
L'écriture d'une fonction rend un programme plus simple à comprendre, plus facile à vérifié et plus simple à modifier.
Vous avez déjà utilisé certaines fonctions pré programmé sans le savoir : print(); input(), randint()...

Les fonctions font partie des routines. Ce sont des portions de programme auxquelles on a donné un nom, afin de pouvoir les utiliser ensuite en rappelant juste ce nom.
Une chose à retenir, la redondance du code est l'ennemi numéro un du programmeur ! Il faut à tout prix éviter d'écrire plusieurs fois le même code dans son programme !
Vous découvrirez assez vite les raisons avec l'expérience. Mais multiplier le même code complique la maintenance et accroît fortement le risque d'erreur!
Sans oublier que cela fait plus de boulot, car plus de code à écrire

Revenons à l'utilité des fonctions.
Une fonction est utilisée comme une boite noire : on fournit des valeurs et on récupère "quelque chose". C'est très pratique et nous permet d'utiliser du code écrit par quelqu'un d'autre.

```python
valeur=randint(1,5)
```
Ici, je fournis deux valeurs à ma fonction : 1 et 5 et la fonction me renvoie un nombre aléatoire dans cet intervalle. C'est magique, et je n'ai pas la moindre idée de ce qu'il se trouve dans la fonction randint(). J'ai juste besoin de connaître ces paramètres d'entrée et de sortie !

## Définir une fonction
Une fonction est définie par un nom, éventuellement des paramètres d'entrée (pas obligatoire), et une sortie (pas obligatoire non plus) puis en donnant le code de cette fonction. (bloc)

**Déclaration d'une fonction**
```python
def ma_Fonction(param1,param2):
  #contenu de ma fonction
  return valeurSortie
```
La déclaration de fonction suit une syntaxe particulière en python.
Elle commence par le mot-clé **def** suivie du nom de la fonction.
Le nommage d'une fonction suit les mêmes restrictions que ceux des variables. (alphanumérique, pas de caractères spéciaux...)
Puis entre parenthèses une liste de paramètres d'entrée suivie de **:**

Le contenu de ma fonction (bloc d'instruction) doit être indentées
Enfin, une fonction peut renvoyer une valeur. On parle alors de valeur de sortie.
Pour cela, on utilise le mot-clé **return** suivie de la valeur de sortie.
Attention l'instruction _return_ stop l'exécution de la fonction la suite de la fonction ne sera donc pas exécuter.



```python
def addition(val1,val2):
  somme = val1 + val2
  return somme
```

_N'appeler pas vos fonctions par le même nom qu'une de vos variables déjà existant, sous peine d'obtenir des résultats aberrants, car l'ordinateur risque de confondre les deux._


**Utiliser une fonction**

L'utilisation d'une fonction est très simple, vous l'avez déjà fait : il suffit d'utiliser son nom avec ces paramètres :
```python
somme = addition(10,12)
print("message")
valeur = input()
```

## Arguments d'une fonction
Une fonction peut comporter plusieurs arguments (appelés aussi paramètre). Il suffit de séparer par une virgule les différents arguments.



```python
def fonctionSansArgument():
  return 10

def fonctionAvecUnArgument(param1):
  return param1+10

def fonctionAvecPlusieurArgument(v1,v2,v3,v4):
  return v1+v2+v3+v4    
```
Un argument de fonction permet d'utiliser des "éléments" du programme extérieurs.
Le contenu d'une fonction appelé "corps" de la fonction se situe dans un environnement un peu particulier. Celui-ci contient les valeurs des variables définit hors de la fonction, mais ne peut pas les modifier.
_On verra plus tard que ce n'est pas complétement vrai, mais pour l'instant, je préfère que vous reteniez ceci, la manipulation de vos variables non pas d'impacte en dehors de votre fonction_

On utilise alors le terme de **variable local** et **variable global**

Reprenons notre toute première analogie de l'étagère de rangement.
Lorsque nous écrivons du code dans une fonction, nous nous situons dans une autre chambre avec **exactement** la même étagère possédant les mêmes objets, ranger dans le même ordre.
On parle ici de variable globale. Global, car elles sont accessibles dans tout le programme (y comprit dans les autres chambres).
Mais attention ce ne sont pas les mêmes objets, ce sont des sortes de copies ! Vous êtes dans une autre chambre et si vous modifiez le contenu d'une case dans votre nouvelle chambre, cela n'affectera pas la chambre principale.

```python runnable
variableGlobal = 10

def ma_fonction():
  variableGlobal = 20
  print(variableGlobal)

ma_fonction()
print(variableGlobal)
```
Si vous exécutez le code ci-dessus vous voyez bien que _variableglobal_ possède la valeur 20 dans la fonction _ma_fonction_ mais garde la valeur 10 en-dehors.

Si dans votre nouvelle chambre vous décidez de rajouter des objets (variable) on parle alors de **variable local** car elle est locale à votre nouvelle chambre uniquement.
L'étagère de votre chambre principale n'est pas modifiée et ne possède pas ce nouvel objet.




```python
def ma_fonction():
  variableLocal = 20

ma_fonction()
print(variableLocal)
```
_l'exécution du code ci-dessus renverra une erreur : variablelocal n'est pas définie et n'existe pas_

Mais alors comment je fais si je souhaite modifier la valeur de mes variables globales ?
Pour cela, il existe une solutions :

Le paramètre de sortie !!!

Si je souhaite modifier une variable globale, je peux simplement la réaffecter à la valeur de sortie de mon programme !
```python
valeurGlobal = 10
def ma_fonction(v1):
  v1 +=10
  return v1
valeurGlobal = ma_fonction(valeurGlobal)
```

L'instruction return permet de sortir de ma fonction et de renvoyé une valeur. Cette valeur peut très bien être la valeur d'une variable local.
C'est un peu comme si on rapportait de notre nouvelle étagère un objet à stocker dans notre étagère principale!
Une fois sortie de la fonction les *variable local* sont "détruite"!



## Point important à propos des fonctions :

**Respecter la syntaxe**

Il est impératif de bien respecter la syntaxe de déclaration :
Mot-clé **def** ne pas oublier **:**
Et faire attention à l'indentation!!
Car c'est l'indentation qui indique la fin de notre fonction
```python
def ma_fonction():
  #je suis dans ma fonctions
  #toujours
  return 0
  #je suis encore dans ma fonctions
print("out") #fin de l'indentation je ne suis plus dans ma fonction
```

**Respecter l'ordre et le type des arguments d'entrée !**
Lorsque on appelle une fonction, il est impératif de passer les arguments dans le bon ordre !
Ainsi que le type attendu !



```python
def ma_fonction(param1,param2):
  for i in range(param1):
    print("bonjour je suis " + param2)
```

l'appel ma_fonction ("remi",10) ne fonctionnera pas alors que ma_fonction (10,"remi") sera bon

**return permet une sortie de fonction**
Une fonction peut contenir plusieurs return (notamment dans le cas de test if). Cependant dès qu'une instruction _return_ est exécutée, les lignes suivantes ne sont plus lues.
```python
def ma_fonction(val1):
  if (val1%2)==2:
    return "pair"
  else:
    return "impaire"
  return "ceci est un return jamais lu"  
```
