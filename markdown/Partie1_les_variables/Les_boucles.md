# Répétez des tâches facilement à l’aide de boucles
Au contraire de l'humain, l'une des choses que les machines font le mieux est la répétition sans erreur de tâches identiques.
Et cela tombe bien car il s'agit l'un des derniers fondamentaux de l'algorithmie: les boucles.
Il existe bien des méthodes pour programmer ces tâches répétitives, alors commençons par la base:

## Boucle bornées (For)
Présente dans tout les langagues de programmation, les boucles permettent de répéter des bloc d'instruction.
Python propose deux type de boucles:
+Les boucles bornées (for)
+boucles non bornées (while)

Commencont par la première:
```python
for i in range(0,10):
  bloc A
```
la boucle **for** permet de repeter un nombre précis de fois un bloc d'instruction.
Dans notre exemple ci-dessus le bloc A sera repéter 10 fois
On dit également que l'on itére x fois le bloc A.
La variable i va d'ailleur possédez la valeur de l'iteration.On parle alors d'**enum** ou **itérateur** (à retenir car cela nous sera bien utile plus tard).
A chaque tour de boucle,c'est à dire à chque exécution du bloc A, la variable indiquée apres le for( ici i) augmente de 1.


```python
for i in range(10):
  print(i)
```
ici nous affichons donc dans l'ordre 0,1,2,3,4,5,6,7,8,9.
__les plus attentif noterons que range(0,10) est devenu range(10)__
__en python la fonction range commence par défaut à 0 il est donc pas obligatoire de le préciser__

Vous noterez que l'affichage s'arréte à 9 et commence par 0. La boucle s'arréte lorsque la comparaison est vrai (i==10).
Et il ne commence pas par 1 mais par 0!!! Ceci est vrai dans tout les langagues informatique
**Il s'agit de l'erreur la plus commune en informatique** surtout lorsque l'on débute.
Je vous conseil de bien mémoriser ceci, et d'y penser à chaque fois que vous écrirez une boucle lorsque vous développerez des programmes.

Il est possible de commencez par une valeur différente de zero:
```python runnable
for i in range(10,15):
  print(i)
```

voire d'incrémenter par une valeur différente que 1
__dans ce cas il est obliger de préciser sa valeur de départ__

```python runnable
for i in range(0,10,2):
  print(i)
```

voir de décrémenter:
```python runnable
for i in range(10,0,-1):
  print(i)
```
Vous l'aurez comprie, les deux premiere valeur de range corréspond à valeur de départ , valeur d'arriver. la 3em valeur corréspond à la valeur d'itération




## boucle non bornée (while)

La seconde méthode permettant de répéter un bloc d'instruction est la boucle while.
Cette méthode permet d'exécuter un bloc d'instruction **tant que** une expréssion booléenne est vrai

```python
i=0
while i<10:
  i+=1
  bloc A
```

__ici il ne faut pas oublié d'initialiser la variable i, car contrairement à la boucle for la boucle while ne touche pas au variable__

l'extrait ci dessus éxécutera le bloc A tant que la condition i<10 n'est pas remplie.
**n'oubliez pas d'incrémenter vos variables lors de l'utilisation de boucle while sans quoi vous allez découvrire les joies de la boucles infinies**

```python runnable
a=10
b=2
while b<10:
  b = b*2
  print(b)
```

Le mieux pour comprendre ces deux conceptes c'est encore de pratiquer!
