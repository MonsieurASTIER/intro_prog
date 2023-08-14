#QCM
vous connaissez la routine maintenant.Validons les nouvelles connaissances avec un QCM

```python
  def affiche_variable(val1):
    print(val1)

```
?[Qu'elle est le nom de ma fonction?]
- [] def
- [] affiche
- [X] affiche_variable
- [] val1
- [] elle n'a pas de nom

?[Combien posséde t'elle d'argument en entrée]
- [] 0
- [X] 1
- [] 2
- [] 3

---
---

```python
  def ma_fonction(val1):
  val1+=1
  return val1
```

?[La fonction ma_fonction est t'elle bien ecrite]
- [] oui
- [X] non
---
---

```python
  def ma_fonction2(val1 val2 val3):
  val1+=1
  return val1
```

?[La fonction ma_fonction2 est t'elle bien ecrite]
- [] oui
- [X] non
---
---

```python
  def ma_fonction3(val1,val2,val3):
    return val1+val2+val3
```
?[La fonction ma_fonction2 est t'elle bien ecrite]
- [X] oui
- [] non

---
---


```python
  def ma_fonction4(val1):
    if val1<2:
      return 1
    elif val1<4:
      return 2    
    return 3
```

?[que renvoie l'appel ma_fonction(0)]
- [] 0
- [X] 1
- [] 2
- [] 3

?[que renvoie l'appel ma_fonction(3)]
- [] 0
- [] 1
- [X] 2
- [] 3

?[que renvoie l'appel ma_fonction(30)]
- [] 0
- [] 1
- [] 2
- [X] 3

---
---


```python
  def ma_fonction(val1):
    val1=val1+1
    return val1

  val1=10
  ma_fonction(val1)  
```
?[Qu'elle est la valeur de val1 à la fin de l'execution de ce programme]
- [] 0
- [X] 10
- [] 11
- [] valeur vide

---
---

```python
  def ma_fonction(val1):
    val1=val1+1
    return val1

  a=10
  b=ma_fonction(a)  
```
?[Qu'elle est la valeur de b à la fin de l'execution de ce programme]
- [] 0
- [] 10
- [X] 11
- [] valeur vide

---
---

```python
  def ma_fonction():
    a=a+1
    return a

  a=10
  b=ma_fonction()  
```
?[Qu'elle est la valeur de b à la fin de l'execution de ce programme]
- [] 0
- [] 10
- [X] 11
- [] valeur vide

?[Qu'elle est la valeur de a à la fin de l'execution de ce programme]
- [] 0
- [X] 10
- [] 11
- [] valeur vide


---
---

## Avant d'aller plus loin
 Il est temps de faire un petit point Très important sur l'écriture des programmes informatique
Il est très rare que vous développez un programme seul, et encore plus que vous soyez le seul à l'utilisez une fois développez (ce serait dommage).
Lors de l'écriture d'un programme entier, il est important de penser à la réutilisabilité de votre programme, et du faite que d'autre développeur que vous sera amener à lire votre code. Il est donc important de commenter vos programme et de rediger une documentation. Pour cette derniere nous verrons plus en détails tard dans l'année.
Par contre je souhaite à partir de maintenant que dés lors vous définissez une fonction vous l'accompagner d'un **DocString**

**DocString**
Le mot docstring est un raccourci pour DOCumentation STRINGs. On les utilise pour décrire le comportement d'une fonction et donnée des instructions sur son utilisation.
Une docstring se définit à l’intérieur d'une fonction, directement après ça déclaration

```python
  def fonction_cube(param1):
    """description rapide de ma fonction
      Parametre:
        param1 (int): descrpition du parametre 1
      return (type): description de la valeur retourner
    """
    return param1
```

**Je souhaite qu'a partir de maintenant chaque fonction que vous écrivez soit composé d'une DocString**

Lorsque vous aller utiliser des fonctions qui ne sont pas les votres (que vous n'avez pas vous même coder), comme un module extèrieure (c'est un groupe de fonction provenant d'un autre programme. Vous en avez déjà utiliser: _randint()_ du module _random_) vous pouvez afficher la docstring de cette fonction grace à print(mafonction.__doc__)


---
---

**Programme 1**
Ecrire une fonction qui prend deux argument en entrer et renvoie la valeur du plus grand des deux arguments

**Programme 2**
Ecrire une _perimetre_ permettant de calculcer le périmètre d'un cercle. La fonction admettra en entrée variable r correspondant au rayon du cercle

**Programme 3**
Ecrire une fonction _pair_ qui renvoie True si le nombre passer en paramètre est pair, et False sinon

**programme 4**
Ecrire une fonction _lancer_des_ qui renvoie le résultat d'un lancé de dés avec comme arguments d'entrer le nombre de dés lancer.
_rappel pour generer de l aléatoire utiliser =randint()_

**programme**

Ecrire une fonction _exposant_ qui prend en argument x et n et qui renvoie le résultat de x exposant n

---
---
