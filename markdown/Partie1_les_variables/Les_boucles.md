# Répétez des tâches facilement à l’aide de boucles

Au contraire de l'humain, l'une des choses que les machines font le mieux est la répétition sans erreurs de tâches identiques.
Et cela tombe bien, car il s'agit l'un des derniers fondamentaux de l'algorithmie : les boucles.
Présentes dans tous les langages de programmation, les boucles permettent de répéter des blocs d'instruction.
Python propose deux types de boucles :
+ Les boucles bornées (for)
+ boucles non bornées (while)

## Boucle bornée (For)

Commençons par la première :

```python
for i in range(0,10):
  bloc A
```
La boucle **for** permet de répéter un nombre précis de fois un bloc d'instruction.
Dans notre exemple ci-dessus, le bloc A sera répéter 10 fois
On dit également que l'on itère x fois le bloc A.
La variable i va posséder la valeur de l'itération. On parle alors d'**enum** ou **itérateur** (à retenir, car cela nous sera bien utile plus tard).
À chaque tour de boucle, c'est-à-dire à chaque exécution du bloc A, la variable indiquée après le for( ici i) augmente de 1.


```python
for i in range(10):
  print(i)
```
Ici, nous affichons donc dans l'ordre 0,1,2,3,4,5,6,7,8,9

_les plus attentifs noterons que range(0,10) est devenu range(10)_
_en python la fonction range commence par défaut à 0 il n'est donc pas obligatoire de le préciser_

Vous noterez que l'affichage s'arrête à 9 et commence par 0. La boucle s'arrête lorsque la comparaison est vraie (i==10).
Et il ne commence pas par 1, mais par 0!!! Ceci est vrai dans tous les langages informatiques
**Il s'agit de l'erreur la plus commune en informatique,** surtout lorsque l'on débute.
Je vous conseille de bien mémoriser ceci, et d'y penser à chaque fois que vous écrirez une boucle lorsque vous développerez des programmes.

Il est possible de commencer par une valeur différente de zéro:
```python runnable
for i in range(10,15):
  print(i)
```

voire d'incrémenter par une valeur différente que 1
_dans ce cas, il est obligé de préciser sa valeur de départ_

```python runnable
for i in range(0,10,2):
  print(i)
```

voir de décrémenter :
```python runnable
for i in range(10,0,-1):
  print(i)
```
Vous l'aurez compris, les deux premières valeurs de range correspondent à valeur de départ , valeur d'arriver et la 3em valeur correspond à la valeur d'itération



## boucle non bornée (while)

La seconde méthode permettant de répéter un bloc d'instruction, est la boucle **while**.
Cette méthode permet d'exécuter un bloc d'instruction **tant que** une expression booléenne est vrai

```python
i=0
while i<10:
  i+=1
  bloc A
```

_ici, il ne faut pas oublier d'initialiser la variable i, car contrairement à la boucle for la boucle while ne touche pas au variable_

l'extrait ci-dessus exécutera le bloc A tant que la condition i<10 n'est pas remplie.
**n'oubliez pas d'incrémenter vos variables lors de l'utilisation de boucle while sans quoi vous allez découvrir les joies de la boucles infinies**

```python runnable
a=10
b=2
while b<10:
  b = b*2
  print(b)
```

Le mieux pour comprendre ces deux concepts, c'est encore de pratiquer !
