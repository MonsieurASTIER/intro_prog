# QCM
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

?[Combien possède t'elle d'argument en entrée]
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

?[La fonction ma_fonction est t'elle bien écrite]
- [] oui
- [X] non
---
---

```python
  def ma_fonction2(val1 val2 val3):
    val1+=1
  return val1
```

?[La fonction ma_fonction2 est t'elle bien écrite]
- [] oui
- [X] non
---
---

```python
  def ma_fonction3(val1,val2,val3):
    return val1+val2+val3
```
?[La fonction ma_fonction2 est t'elle bien écrite]
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

?[Que renvoie l'appel ma_fonction(0)]
- [] 0
- [X] 1
- [] 2
- [] 3

?[Que renvoie l'appel ma_fonction(3)]
- [] 0
- [] 1
- [X] 2
- [] 3

?[Que renvoie l'appel ma_fonction(30)]
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
?[Qu'elle est la valeur de val1 à la fin de l'exécution de ce programme]
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
?[Qu'elle est la valeur de b à la fin de l'exécution de ce programme]
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
?[Qu'elle est la valeur de b à la fin de l'exécution de ce programme]
- [] 0
- [] 10
- [X] 11
- [] valeur vide

?[Qu'elle est la valeur de a à la fin de l'exécution de ce programme]
- [] 0
- [X] 10
- [] 11
- [] valeur vide


---
---

## Avant d'aller plus loin
Il est temps de faire un petit point très important sur l'écriture des programmes informatiques.
Il est très rare que vous développiez un programme seul, et encore plus que vous soyez le seul à l'utiliser une fois développé (ce serait dommage.).
Lors de l'écriture d'un programme entier, il est important de penser à la ré-utilisabilité de votre programme, et du faite que d'autre développeur que vous sera amener à lire votre code. Il est donc important de commenter vos programmes et de rédiger une documentation. Pour cette dernière, nous verrons plus en détails tard dans l'année.
Par contre, je souhaite à partir de maintenant que dès que vous définissez une fonction vous l'accompagner automatiquement d'un **DocString**

**DocString**
Le mot docstring est un raccourci pour DOCumentation STRINGs. On les utilise pour décrire le comportement d'une fonction et donnée des instructions sur son utilisation.
Une docstring se définit à l’intérieur d'une fonction, directement après sa déclaration



```python
  def fonction_cube(param1):
    """description rapide de ma fonction
      Parametre:
        param1 (int): description du paramètre 1
      return (type): description de la valeur retourner
    """
    return param1
```

**Je souhaite qu'à partir de maintenant chaque fonction que vous écrivez soit composé d'une DocString**

Lorsque vous allez utiliser des fonctions qui ne sont pas les vôtres (que vous n'avez pas vous-même coder), comme un module extérieur vous pouvez afficher la docstring de cette fonction grâce à _print(mafonction.__doc__)_

---
---
**Programme 1**
Écrire une fonction _maxi_ qui prend deux arguments en entrer et renvoie la valeur du plus grand des deux arguments

**Programme 2**
Écrire une fonction _perimetre_  permettant de calculer le périmètre d'un cercle. La fonction admettra en entrée variable r correspondant au rayon du cercle.

**Programme 3**
Écrire une fonction _pair_ qui renvoie True si le nombre passé en paramètre est pair, et False sinon

**programme 4**
Écrire une fonction _lancer_des_ qui renvoie le résultat d'un lancé de dés avec comme arguments d'entrer le nombre de dés lancer.
_rappel pour générer de l'aléatoire utiliser =randint()_


**programme 5**
Écrire une fonction _exposant_ qui prend en argument **x** et **n** et qui renvoie le résultat de x exposant n

**programme 6**
Votre boulangerie a grossi, vous désirez écrire un programme Python qui calculera automatiquement le montant de la facture des clients.
Tout client qui achète au moins 5 fois le même article se voit octroyer une remise de 5 % (uniquement sur le montant de l'achat de cet article).
Écrivez un programme qui contient plusieurs fonctions. Ce programme doit demander à l'utilisateur, ça commande et afficher sa facture une fois ça commande terminer.
Il pourra donc commander différents articles et les différentes réductions devront lui être attribuées.

**programme 7**
Nous allons coder le programme de pierre-papier-ciseaux
1. Écrire une fonction _gagnant_ qui prend deux arguments en entrée : correspondant au choix des deux joueurs
et renvoie 1 si c'est le 1er joueur qui gagne 2 si c'est le second et 0 en cas d'égalité.
2. Écrire le programme qui permet de jouer contre l'ordinateur
L'ordinateur jouera de manière aléatoire grâce à la fonction randint()
3. (facultatif) Il est tout à fait possible d'imaginer une fonction IA qui joue au jeu de manière non-aléatoire, mais en fonction de l'ancienne entrée des joueurs.


**Chiffrage de césar**
1. Écrire une fonction _decale_ qui prend en paramètre : lettre(str) et shift(int) cette fonction renvoie la lettre décaler de _shift
Exemple: cryptage("h",1) renvoie "i"
Aide :

```
>>> ord('A')
65
>>> chr(65)
'A'
```

2. Écrire une fonction _crypter_ qui prend en paramètre un mot(str) et shift(int) cette fonction renvoie le mot avec toutes ces lettres décalées de _shift

3. Écrire un programme qui permet de crypter et décrypter une phrase

---
---
