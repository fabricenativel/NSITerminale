
{% set num = 5 %}
{% set theme = "python" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Introduction à la programmation orientée objet",[],0) }}
{{ telecharger("Jupyter Notebook","./notebook/IntroPOO.ipynb")}}

{{ titre_activite("Syntaxe objet en Python",[]) }}

1. On donne le code python suivant :
```python
    class Duree:

        def __init__(self,heures,minutes,secondes):
            self.heures=heures
            self.minutes=minutes
            self.secondes=secondes

        def __str__(self):
            return f"{self.heures}h {self.minutes}m {self.secondes}s"
```

    1. Quelle classe est crée ? Quels sont les attributs des objets de cette classe ?
    2. Quelle méthode est crée pour les objets de cette classe ?


2. Le record du monde du marathon est actuellement de deux heures, une minute et trente neuf secondes, créer à l'aide de la classe ci-dessus un objet `record_marathon` représentant cette durée et l'afficher.

3. Ecrire une méthode `nombre_secondes` qui renvoie le nombre de secondes d'un objet durée. L'utiliser pour afficher le record du monde du marathon en secondes.

4. Ajouter une méthode `ajoute_secondes(nb_secondes)` à la classe  `Duree` qui permet d'ajouter `nb_secondes` à un objet de type durée.

{{ titre_activite("Getters et setters",[]) }}

1. Créer une classe `Eleve` possédant les attributs suivants : nom, prénom, et classe.
2. Instancier cette classe pour créer l'élève `spiderman`, son nom est Parker, son prénom Peter et il est en première 5.
3. Quel est l'effet de l'instruction  `spiderman.classe = 'Terminale 2'` ?

    !!! Important
        Bien que l'instruction précédente soit correcte, elle est contraire à l'esprit de la programmation objet dans lequel l'accès aux attributs d'un objet (ou la modification) devrait toujours se faire par des méthodes de l'objet. On respecte ainsi le principe d'**encapsulation** qui assure que l'utilisation des objets se fait indépendamment de leur structure interne (qui est susceptible d'être modifiée)
        Les méthodes permettant d'accéder à un attribut s'appellent des *getters* (accesseur) et celles permettant de modifier un attribut s'appellent des *setter* (mutateur)

4. Ecrire une méthode permettant d'accéder la classe d'un élève (le *getter*).
5. Ecrire une méthode permettant de modifier la classe d'un élève (le *setter*).
6. Modifier de nouveau (mais cette fois "proprement") la classe de `spiderman`.

## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("Personnage d'un jeu vidéo",[],0) }}

Dans un jeu vidéo, un personnage doit se déplacer dans un environnement à deux dimensions, sa position y est repéré par son abscisse et son ordonnée. D'autre part ce personnage dispose d'un certain nombre de points de vie qui peuvent évoluer durant le jeu. On considère la définition de la classe `Perso` suivante :

```python
    class Perso:

        def __init__(self,nom):
            self.nom = nom
            self.x = 0
            self.y = 0
            self.pv = 100    
```

1. Au départ combien de points de vie possède un personnage ? Et à quel coordonnées du repère est-il positionné ?
2. Lorsqu'un personnage boit une potion de vie, il récupère 10 points de vie mais sans dépasser le maximum de vie qui est 100. Ecrire la méthode `boit_potion` qui implémente ce fonctionnement.
3. Ecrire la méthode `avance(nbcases)` qui permet au personnage d'avancer de `nbcases` vers l'avant.

{{ exo("Modéliser un compte en banque",[]) }}
On modélise un compte bancaire par : <br>
:octicons-triangle-right-16: un numéro de compte <br>
:octicons-triangle-right-16: un nom de titulaire <br>
:octicons-triangle-right-16: un solde (négatif si le compte est débiteur)


1. Ecrire une classe `CompteBancaire` représentant cette modélisation
2. Créer le compte n°421 de M. Tartampion ayant un solde de $-125,10$ € et le compte n° 705 de Mme Untel ayant un solde de $3120,07$ €.
3. Ecrire et tester la méthode spéciale  `__str__` permettant d'afficher l'objet CompteBancaire. Par exemple l'affichage de l'objet représentant le compte bancaire de M. Tartampion donnera : `N°421 - M. Tartampion : -125,10 euros`
4. Ecrire les  méthodes `depot` et `retrait` permettant respectivement d'ajouter ou de retirer une somme d'argent d'un objet CompteBancaire.
5. Ecrire la méthode `virement` permettant de transférer une somme d'argent entre deux comptes. Par exemple si `C1` et `C2` sont deux objets de type `CompteBancaire`, alors `C1.virement(C2,montant)` aura pour effet d'enlever `montant` euros du compte `C1` et de les transférer au compte `C2`.



{{ exo("Un peu de géométrie",["maths"]) }}

On donne la classe `Point` définie ci-dessous qui représente un point du plan par son nom et ses coordonnées dans un repère. Cette classe est déjà dotée d'une méthode d'affichage.

```python
class Point:

    def __init__(self,nom,abcisse,ordonnee):
        self.nom = nom
        self.x = abcisse
        self.y = ordonnee
    
    def __str__(self):
        return f'{self.nom}({self.x};{self.y})'
        
```

1. En utilisant cette classe, créer et afficher les points $A(3;-2)$ et $B(-1;6)$.
2. Ecrire une méthode `milieu(self,other,nom_milieu)` qui renvoie le point milieu du segment ayant pour extrémités les deux points passés en paramètres (`self` et `other`) en lui donnant le nom contenu dans `nom_milieu`. 

    !!! Aide
        On rappelle (mais c'est au programme de classe de seconde) que pour deux points $A(x_A,y_A)$ et $B(x_B,y_B)$  les coordonnes $x_I$ et $y_I$ du milieu $I$ du segment $[AB]$ sont :  
        $x_I = \dfrac{x_A+y_B}{2}$ et $y_I = \dfrac{y_A+y_B}{2}$

3. Utiliser cette méthode pour calculer le milieu $I$ des points $A$ et $B$ définis plus haut et l'afficher. 

    !!! Aide
        Vous devrier obtenir $I(1;2)$

4. Ecrire et tester une méthode permettant de calculer la distance entre deux points.

    !!! Aide
        On rappelle que pour deux points $A(x_A,y_A)$ et $B(x_B,y_B)$ on a $AB = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$.
        D'autre part la fonction racine carrée doit être importée depuis le module `math`

{{ exo("Une classe date",[]) }}

1. Définir et écrire le constructeur  d'une classe `date` possédant trois attributs : `jour`, `mois`, `année`. Ces trois attributs sont entiers, par exemple le 27 octobre 2020 a comme attribut `jour : 27`, `mois : 10` et `année : 2020`. 
2. Affiner le constructeur défini plus haut pour n'accepter que des dates valides, c'est à dire avec un mois compris entre 1 et 12 et le jour ne dépassant pas le nombre de jours du mois.  

    !!! Aide 
        Une idée consiste par exemple à utiliser un dictionnaire contenant les jours de chaque mois : 
        `nb_jours = { 1:31, 2:28, 3:31, 4:30, 5:31 ... } `

    Pour aller plus loin, on pourra tenir compte des années bissextiles de façon à accepter le 29/02/2004 mais pas le 29/02/2005 !

3. Ecrire et tester une méthode spéciale permettant de renvoyer une chaîne de caractères de la forme JJ/MM/AAAA pour la date.
4. Proposer et implémenter un autre format d'affichage par exemple 5 Avril 2005 pour le 05/04/2005.
5. Ecrire et tester une méthode `date.lendemain()` qui retourne le lendemain de l'objet `date`. Par exemple si l'objet `date` correspond au 27/10/2020 alors `date.lendemain()` doit retourner l'objet date correspondant au 28/10/2020.
6. Ecrire et tester la méthode spéciale permettant de tester si une date |`date1` est antérieure à une autre `date2` en écrivant simplement `d1<d2`.

    !!! Aide
        Cette méthode spéciale est `__lt__`

{{ exo("Cartes à jouer",[]) }}

Un jeu de cartes traditionnel contient 32 cartes, chaque carte a une couleur (pique, coeur, carreau ou trèfle) et une valeur (de 7 à 10 puis valet, dame, roi et as).

1. Créer une classe Carte ayant deux attributs : couleur et valeur. 
2. Ecrire une méthode spéciale permettant d'afficher une carte en utilisant le caractère unicode qui la représente. Consulter  la page wikipedia de la  liste des [caractère unicode des cartes](https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode/U1F0A0){target=_blank}.

    !!! Aide
        En python pour afficher le caractère unicode `U+1F0A7`, on peut par exemple écrire  `print(chr(0x1F0A7))`
3. Ecrire une méthode pour comparer deux cartes
4. Utiliser la programmation objet afin de simuler le jeu de la bataille entre deux joueurs.

{{ exo("Module fraction",["maths"]) }}

L'énoncé est au format `pdf`, téléchargeable ci-dessous :

{{ telecharger("Ecriture d'un module fraction","./pdf/C5/C5-exofractions.pdf")}}


{{ exo("Cryptage selon le code de César",["bac"]) }}

Dans cet exercice, on étudie une méthode de chiffrement de chaînes de caractères alphabétiques. Pour des raisons historiques, cette méthode de chiffrement est appelée "code de César". On considère que les messages ne contiennent que les lettres capitales de l’alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ" et la méthode de chiffrement utilise un nombre entier fixé appelé la clé de chiffrement.

1. Soit la classe `CodeCesar` définie ci-dessous :

```python
    class CodeCesar:

        def __init__(self, cle):
            self.cle = cle
            self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def decale(self, lettre):
            num1 = self.alphabet.find(lettre)
            num2 = num1+self.cle
            if num2 >= 26:
                num2 = num2-26
            if num2 < 0:
                num2 = num2+26
            nouvelle_lettre = self.alphabet[num2]
            return nouvelle_lettre
```

On rappelle que la méthode `str.find(lettre)` renvoie l'indice (index) de la `lettre` dans la chaîne de caractères `str`

**Représenter** le résultat d'exécution du code Python suivant :
```python
code1 = CodeCesar(3)
print(code1.decale('A'))
print(code1.decale('X'))
```
2. La méthode de chiffrement du « code César » consiste à décaler les lettres du message dans l’alphabet d'un nombre de rangs fixé par la clé. Par exemple, avec la clé 3, toutes les lettres sont décalées de 3 rangs vers la droite : le A devient le D, le B devient le E, etc.

**Ajouter** une méthode `cryptage(self,texte)` dans la classe `CodeCesar` définieà la question précédente, qui reçoit en paramètre une chaîne de caractères (le message à crypter) et qui retourne une chaîne de caractères (le message crypté). 
 
Cette méthode `cryptage(self, texte)` doit crypter la chaîne texte avec la clé de l'objet de la classe CodeCesar qui a été instancié.

Exemple :

```python
>>> code1 = CodeCesar(3)
>>> code1.cryptage("NSI")
'QVL'
```
3. **Ecrire** un programme qui : <br>

:octicons-dot-fill-16: demande de saisir la clé de chiffrement <br>
:octicons-dot-fill-16: crée un objet de classe `CodeCesar`<br>
:octicons-dot-fill-16: demande de saisir le texte à chiffrer<br>
:octicons-dot-fill-16: affiche le texte chiffré en appelant la méthode `cryptage`  <br>

4- On ajoute la méthode `transforme(texte)` à la classe `CodeCesar` :

```python
def transforme(self, texte):
    self.cle = -self.cle
    message = self.cryptage(texte)
    self.cle = -self.cle
    return message
```
On exécute la ligne suivante : `print(CodeCesar(10).transforme("PSX"))`

**Que va-t-il s'afficher ? Expliquer** votre réponse.