
{% set num = 6 %}
{% set theme = "sd" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Notebook d'introduction",[],0) }}
{{ telecharger("Jupyter Notebook","./notebook/StructuresLineaires.ipynb")}}


## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("Choix d'une structure de données",[],0) }}

Dans chacune des situations suivantes, indiquer en justifiant votre réponse, quelle structure de données pourrait être adoptée :

1. La gestion du bouton "Revenir à l'étape précédente" d'un logiciel de retouche d'images.
2. Une application permettant de gérer une liste de courses dans laquelle on peut ajouter/supprimer/modifier des éléments.
3. L'envoi de travaux d'impression à une imprimante.
4. La représentation dans un programme d'un plateau de jeu (comme un équiquier ou un damier) dont on connaît à l'avance les dimensions.
5. La saisie d'une ligne de commande dans un terminal où on ne peut utiliser que la touche retour arrière pour éditer ses commandes

{{ exo("Le module `deque` de Python",[]) }} 
Bien que Python ne propose pas de façon native le type abstrait de donnée file, le module `collections`  permet d'importer `deque` (**d**ouble **e**nded **que**ue). Cette structure de données permet l'insertion ou la suppression aux deux extrémités en temps constant (donc en $O(1)$). Elle correspond à des listes chaînées disposant d'un accès direct au premier et au dernier élément (d'où le nom *double ended*). L'insertion d'un élément en début d'un objet de type `deque` s'effectue à l'aide de la méthode `appendleft` et la suppression d'un élément en fin s'effectue (comme pour les listes de Python) à l'aide de la méthode `pop`.

1. Importer `deque` depuis le module `collections`, et écrire puis tester une nouvelle implémentation de file utilisant un objet de type `deque` plutôt qu'une liste.

    !!! Aide
        La fonction `len` existe sur les objets de type `deque` et pourra être appelée pour tester si la file est vide.

2. Vérifier que cette nouvelle implémentation est plus efficace que l'implémentation sous forme de liste vue ci-dessus.

    !!! Aide
        Comparer par exemple les temps d'exécution pour enfiler puis defiler les entiers de 1 à un cent mille.

3. Reprendre ce qui a été vu dans le notebook d'introduction à ce chapitre et tracer les graphiques de temps d'exécution en fonction de la taille de la file. 
4. Compléter cette nouvelle implémentation par les méthodes suivantes :

    1. Un attribut `taille` ainsi qu'une méthode `get_taille` permettant de lire le nombre d'éléments dans la file.
    2. Une méthode d'affichage d'un objet file  (séparer les éléments  par des virgules et choisir les caractères de début et de fin). 

        !!! Aide 
            Les objets de type `deque` autorisent l'accès par indice avec la notation crochet (comme les listes de Python).

    3. Un attribut `taille_max` fixant une taille maximale pour la file, si cette taille est dépassée, on ne peut plus enfiler.

5. Dans la documentation du module `deque` on peut lire : *"L'accès par indice est en O(1) aux extrémités mais en O(n) au milieu. Pour des accès aléatoires rapides, il est préférable d'utiliser des listes.*". Justifier rapidement, par exemple par un schéma, ces remarques sur la complexité des opérations et la comparaison avec les listes de Python.

{{ exo("Manipulation d'une pile",[]) }}

On suppose qu'on dispose d'une pile notée `P` et de son interface usuelle, c'est à dire :

* `est_vide`,
* `empile` et
* `depile`.

Ecrire une fonction qui échange les deux éléments, situés au sommet de la pile. Si la pile contient moins de deux éléments, la fonction ne fait rien.
Par exemple si la l'état de la pile est `|a,b,c,d>`, elle devient `|a,b,d,c>` comme illustré sur le schéma ci-dessous : 
![Inversion des deux éléments situés au sommet d'une pile](./images/C6/pileinv.png){: .imgcentre}

!!! Attention
    On ne doit utiliser **que** l'interface d'une pile par conséquent la notation usuelle de Python avec les crochets pour accéder aux éléments d'une liste n'est pas autorisée !

{{ exo("Retour sur l'implémentation d'une pile",[])}}
On revient sur l'implémentation d'une pile en Python à l'aide de la {{sc("poo")}} (déjà vu dans le notebook d'introduction à ce chapitre) : 
```python
class Pile:
    
    def __init__(self):
        self.contenu = []
    
    def empiler(self,element):
        self.contenu.append(element)
        
    def est_vide(self):
        return self.contenu==[]
 
    def depiler(self):
        assert not self.est_vide(), "Pile vide"
        return self.contenu.pop()
```

1. Recopier et enregistrer cette implémentation de façon à disposer d'un module `Pile` que nous pourrons utiliser par la suite.
2. Dans cette implémentation, la pile est représentée par une liste de Python, le sommet de la pile est-il le début ou la fin de cette liste ? Ce choix est-il judicieux ? Justifier votre réponse.
3. Compléter cette implémentation en ajoutant :

    1. Une méthode d'affichage en séparant les éléments par des virgules et en adoptant les caractères de votre choix pour le début et la fin de la pile.

        !!! Aide
            Pour le problème de la virgule après le dernier élément, on peut utiliser un **slice** pour l'enlever, ou alors faire un test permettant de ne pas mettre de virgule lors qu'on atteint le dernier élément.

    2. Une méthode `sommet`, permettant de lire la valeur situé au sommet de la pile *sans l'enlever*.
    3. Un attribut `taille` à la pile indiquant le nombre d'éléments contenus dans la pile.
    4. Un attribut `taille_max` à la pile, lorsque cette taille est dépassée, on ne peut plus empiler. 

        !!! Aide
            Le module `math` de Python propose la constante `inf` pour simuler l'infini, on pourra donner cette valeur par défaut à `taille_max` de façon à avoir une pile de taille "infinie" lorsque le paramètre `taille_max` n'est pas donné.

4. En utilisant le module `Pile`, écrire une fonction Python qui prend en entrée une liste et renvoie cette liste retournée. Par exemple `retourne([1,2,3])` renvoie `[3,2,1]`.

    !!! Aide
        On rappelle (voir activité) qu'il suffit d'empiler les éléments de la liste puis de les dépiler.

{{ exo("Expression bien parenthésée",[]) }}
On dit qu'une expression est bien parenthésée lorsque chaque parenthèse ouvrante est associée à une unique parenthèse fermante et inversement. Par exemple, on a souligné dans l'expression suivante le problème de parenthésages : 
$(3+2)\textcolor{red}{\underline{)}}-(4+1)$

1. Les expressions suivantes sont-elles bien parenthésées ? Sinon, indiquer l'emplacement dans la chaîne de caractères où l'erreur est détectée.
    1. $3+(5-4\div(3+2)))+10$
    2. $((3+2)\times 5$ 
    3. $5)-4\times2($ 
    4. $((3+2)\times(5-3))$

2. Ecrire une fonction `bien_parenthesee` qui prend en argument un expression (sous la forme d'une chaine de caractères) et qui renvoie $-1$ lorsque l'expression est bien parenthésée et sinon un entier indiquant l'emplacement dans l'expression où l'erreur de parenthésage est détectée.

    !!! Aide
        On pourra, parcourir l'expression et utiliser une pile qui stocke les indices de chaque parenthèses ouvrante. On dépile, lorsqu'on rencontre une parenthèse fermante.

3. Tester votre fonction sur les expressions de la question **1.**
4. Utiliser cette fonction afin de produire un affichage de l'erreur à la façon de Python c'est à dire avec un caractère `^` en dessous de l'erreur. Par exemple  : $(2+3)\underset{\textcolor{red}{\wedge}}{)}-5$

5. Poursuivre ce travail en travaillant sur des expressions pouvant contenir simultanément d'autres types de parenthèses, par exemple : `[]` ou encore `{}`.

{{ exo("Implémentation naïve d'une file",[])}}
On souhaite implémenter une file en Python à l'aide d'une liste de Python et de la {{sc("poo")}} à la façon de ce qui a été fait pour les piles dans l'exercice **4**.

1. Recopier et compléter le code ci-dessous de façon à ce qu'on enfile un élément en l'ajoutant en début de liste. (et que donc on défile en enlevant en fin de liste.
```python
class File:
    
    def __init__(self):
        self.contenu = []
    
    def enfiler(self,element):
        self.contenu = .............
        
    def est_vide(self):
        return self.contenu==[]
 
    def defiler(self):
        assert not self.est_vide(), "File vide"
        return self.............
```
2. Tester cette implémentation en créant une file dans laquelle on enfilera puis défilera les entiers de 1 à 100.
3. Reprendre le test précédent en mesurant les performances du programme pour les entiers jusqu'à cent mille.
    
    !!! Aide
         Par souci de simplicité, on utilisera la fonction `time` du module `time` (même si le temps d'exécution mesuré dépend d'autres facteurs).

4. Cette implémentation est-elle satisfaisante en terme de complexité des opérations ? Justifier.
5. Même question si on décide, plutôt d'enfiler en fin de liste (et donc de défiler en début).


{{ exo("Implémentation d'une file avec deux piles",[]) }}
On considère la file suivante  :
![file](./images/C6/file1.png){: .imgcentre}
On peut aussi la schématiser  sous la forme de deux piles :
![file](./images/C6/file2.png){: .imgcentre}
Pour comprendre ce fonctionnement, on part d'une file vide et on montre par quelques exemples l'état de la file et des deux piles qui la représente : 

| Etape | Opération | Etat de la file | Pile d'entrée | Pile de sortie |
|-------|-----------|-----------------|---------------|----------------|
|:one:  | Enfiler `a` |  `>a>` |  `|a>` | `|>`  
:two: | Enfiler `b` | `>b,a>` |`|a,b>` |`|>`  
:three: |Enfiler `c` | `>c,b,a>` |`|a,b,c>` |`|>`  
:four: |Defiler |`>c,b>`  |`|>` |`|c,b>` 
:five: |Defiler |`>c>`  |`|>` |`|c>` 
:six: |Enfiler `d` |`>d,c>` |`|d>` | `|c>` 


!!! Aide
    Observer attentivement ce qui se passe à l'étape :four: : la pile de sortie étant vide, la *totalité* de la pile d'entrée est dépilé dans la pile de sortie.


1. Compléter le tableau ci-dessous avec les étapes suivantes :

    1.  Defiler 
    2.  Enfiler `e`
    3.  Defiler
    
2. Recopier et compléter : <br>
Une file peut s'implémenter en gérant .... pile :

    * enfiler un élément revient à .......... dans une pile d'entrée
    * defiler un élément revient à ............. d'une pile de sortie  (cette pile est ........... au départ)
    * Si la pile de sortie est  ............ on .......... la totalité de la pile ........... dans ...................

3. Ecrire en Python une implémentation d'une file sous la forme de deux piles en utilisant la {{ sc("poo")}}.
4. Tester votre implémentation (reprendre éventuellement les opérations :one: à :six: en faisant afficher l'état de la file et des deux piles à chaque étape). 

    !!! Lien "Pour aller plus loin"
        Rechercher la complexité des opérations de cette implémentation (hors programme).


{{ exo("Buffer",[]) }}
On considère le programme Python suivant :
```python
fic1 = open("sortie.txt","w")
fic1.write("Python a écrit ici")
fic2 = open("sortie.txt","r")
contenu = fic2.read()
fic1.close()
fic2.close()
print(contenu)
```

1. La mémoire tampon

    1. Que fait ce programme et quel résultat devrait produire l'affichage de la variable {\tt contenu} ?
    2. Recopier et executer ce programme, le résultat est-il celui attendu ?
    3. L'écriture dans un fichier est géré par Python à l'aide d'une mémoire tampon (*buffer* en anglais), Python attend que ce buffer atteigne une certaine taille (ou que le fichier soit fermé) avant d'écrire de façon effective dans le fichier, ce qui explique le fonctionnement ci-dessous. Selon vous, pourquoi cette gestion du `write` via un *buffer* ?
    4. On peut forcer l'écriture sans attendre que le *buffer* soit plein grâce à la méthode `flush` des descripteurs de fichiers. Insérer `fic1.flush()` après l'instruction `write` du programme ci-dessous et l'exécuter de nouveau pour constater la différence.
    
2. Simuler un *buffer* 
On considère le programme suivant qui écrit des nombres tirés au hasard dans un fichier *sans utiliser de buffer*, c'est à dire qu'on force l'écriture de chaque nombre à l'aide de `flush`:
```python
from random import randint
from time import time

# Création liste de nombres à écrire
SIZE = 100000
nombres = [randint(1,SIZE) for _ in range(SIZE)]

debut = time()
fic = open("sortie.txt","w")
for nb in nombres:
    fic.write(str(nb)+'\n')
    fic.flush()
fic.close()
fin = time()
temps = fin-debut
print("Temps sans buffer ",temps)
```

    1. Recopier et exécuter ce programme et en noter le temps d'exécution
    2. A quel type de structure de données correspond un *buffer* ?
    3. Ecrire une seconde version de ce programme en simulant l'utilisation d'un buffer, c'est à dire qu'on enregistre dans une structure de données les nombres à écrire et qu'on attend que cette structure soit pleine pour écrire tous les éléments en une fois (on pourra créer une constante `BUFFER_SIZE`).
    4. Comparer le temps d'exécution de cette nouvelle version avec celui du programme précédent.


{{ exo("Comparaison de plusieurs implémentation du TAD liste",[]) }}
On rappelle l'implémentation du TAD liste sous forme de liste chaînée vue dans le notebook d'introduction à ce chapitre :
```python
class Maillon:
    '''Le maillon d'une liste chainée représenté par sa valeur et un lien vers le maillon suivant'''
    def __init__(self,valeur):
        self.valeur = valeur
        self.suivant = None
        
class Liste:
    '''Une liste est un lien vers son premier maillon'''
    
    def __init__(self):
        self.tete = None
    
    def est_vide(self):
        return self.tete==None
        
    def ajoute(self,valeur):
        nouveau_maillon = Maillon(valeur)
        nouveau_maillon.suivant = self.tete
        self.tete = nouveau_maillon
    
    def supprime(self):
        assert not self.est_vide(),"Liste vide, suppression impossible"
        self.tete = self.tete.suivant
```

1. Compléter cette implémentation en ajoutant une méthode d'affichage.
2. Ajouter une méthode `tete` qui renvoie la valeur du maillon situé en tête de liste.
3. Le type *list* de Python est aussi une implémentation de ce TAD. Quelles opérations sur le type *list* de Python correspondent à `ajoute` et `supprime` définis ci-dessus ?
4. Compléter le tableau suivant permettant de comparer en terme de complexité diverses implémentations du type abstrait de données liste: 

    | Opération | *list* (type Python) | class Liste | Module deque
    |-----------|----------------------|---------------|---------------
    |Insertion en tête | ...... | ...... | ...... 
    |Ajout en queue | ...... | ...... | ...... 
    |Accès à un élément | ...... | ...... | ...... 

{{ exo("Exercices extraits de sujet de bac",["bac"]) }}

1. {{ telecharger("Amérique du nord 2021 - exercice 5","./pdf/C6/AmeriqueNord2021-exo5.pdf") }}

2. {{ telecharger("Métropole CL 2021 - exercice 2","./pdf/C6/MetropoleCL2021-exo2.pdf") }}

3. {{ telecharger("Métropole sujet 2 2021 - exercice 5","./pdf/C6/Metropole2021-exo5.pdf") }}