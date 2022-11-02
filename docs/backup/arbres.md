
{% set num = 8 %}
{% set theme = "sd" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Vocabulaire",[],0) }}

1. Après execution d'une commande dans un terminal Linux on a obtenu l'affichage ci-dessous :
![arborescence de repertoires](./images/C8/arborescence.png){: .centre}

    1. De quelle commande s'agissait-il ? Quelle est sa traduction en français ?
    2. Que sont `Maths` et `NSI` pour le système d'exploitation ?
    3. Un point (**.**) figure en haut du schéma, quelle en est la signification ?
    4. Que signifie le lien entre `NSI` et `Projet` ?

2. Le schéma ci-dessus est un exemple d'**arbre** (on parle d'ailleurs de l'arborescence des dossiers dans un système d'exploitation). Un arbre est constitué de **noeuds** et un lien entre deux noeuds s'appelle une **arête**.

    1. Citer trois noeuds de l'arbre ci-dessus et donner un exemple d'arête.
    2. Quel noeud est le répertoire parent de `Systèmes`  ? On dira dans le vocabulaire des arbres que le noeud `Systèmes` est un **fils** de ce noeud.
    3. Citer tous les fils du noeud `NSI`.
    4. Dans un arbre, un seul et unique noeud n'est le fils de personne, on l'appelle la **racine** de l'arbre. De qui s'agit-il ici ?
    5. Nommer les noeuds n'ayant aucun fils (on les appelle **feuilles** de l'arbre).
    6. Une **branche** est une suite (finie) de noeuds depuis la racine vers une feuille. Donner une branche de cette arbre constituée de trois noeuds.
    7. Donner la **taille** de cet arbre (c'est à dire son nombre de noeuds).
    8. Donner l'**arité** de cet arbre, c'est à dire le nombre maximal de fils qu'un noeud peut avoir.
    9. Donner la **hauteur** de cet arbre c'est à dire le nombre maximal de noeuds dans une branche.

        !!! Attention
                La hauteur d'un arbre est parfois définie comme le plus grand nombre d'arêtes dans une branche. Dans les sujets de {{sc("bac")}} faire attention à la définition utilisée qui est normalement donnée dans l'énoncé.



{{ titre_activite("Arbre binaire",[])}}

Chez les abeilles, le système de reproduction fait que :

* une abeille femelle est issue de deux abeilles, un mâle et une femelle,
* une abeille mâle est issue d'une seule abeille femelle.


Cela s'explique par le fait qu'un oeuf non fécondé (donc issu uniquement d'une femelle) donne toujours naissance à une abeille mâle, alors qu'une oeuf fécondé (donc issu d'un mâle et d'une femelle) donne toujours naissance à une abeille femelle. On a représenté ci-contre les quatre premiers niveaux de l'arbre généalogique d'une abeille mâle en notant avec la lettre **M** les mâles et la lettre **F** les femelles.

<div class="centre">

```mermaid
    graph TD
    F0["F"] --> F1["F"]
    F0["F"] --> M1["M"]
    M1 --> F2["F"]
    F1 --> M2["M"]
    F1 --> F3["F"]
    F2 --> F4["F"]
    F2 --> M3["M"]
    M2 --> F5["F"]
    F3 --> F6["F"]
    F3 --> M4["M"]
```
</div>


1. Définition des arbres binaires  

    1. Recopier et compléter cet arbre en ajoutant le 5^e^ niveau.
    2. Rappeler la définition de l'*arité* d'un arbre et d'un noeud. Quelle est l'arité des feuilles d'un arbre ?
    3. Déterminer le degré (arité) des noeuds qui ne sont pas des feuilles selon que le noeud représente une abeille male ou une abeille femelle.
    4. On appelle **arbre binaire**, un arbre dans lequel les noeuds ont au maximum deux fils. Donner une définition équivalente utilisant le mot *arité* et justifier rapidement que l'arbre généalogique d'une abeille est binaire.

2. Une définition récursive
On reprend l'exemple de l'abre généalogique d'une abeille femelle jusqu'au cinquième niveau dessinée ci-dessus. On appelle *sous arbre gauche* et *sous arbre droit* l'arbre généalogique de chacune des deux parents de la racine. L'arbre est alors noté sous la forme d'un triplet constitué de la racine et des deux sous arbres : `(racine, sous arbre gauche, sous arbre droit)`. 

    1. Justifier rapidement que les deux sous arbres sont des arbres binaires.
    2. Que dire du sous arbre droit lorsque l'abeille est un mâle ?
    3. Pour une feuille, que dire du sous arbre droit et du sous arbre gauche ?
    4. En déduire une version récursive de la définition d'un arbre binaire.
    5. Donner une définition récursive de la taille d'un arbre binaire.
    6. Donner une définition récursive de la hauteur d'un arbre binaire.

{{ titre_activite("Relation entre la hauteur et la taille d'un arbre binaire",[])}}

1. On note $h$ la hauteur d'un arbre binaire et $n$ sa taille, on suppose dans la suite que $n \geq 2$. En rappelant les définitions de la hauteur et de la taille d'un arbre, justifier que $n \geq h$.
2. On numérote les noeuds d'un arbre binaire de la suivante :  

    * la racine porte le numéro 1,
    * le fils gauche d'un noeud porte le numéro de son père suivi d'un 0,
    * le fils droit d'un noeud porte le numéro de son père suivi d'un 1.

On a entamé la numérotation de l'arbre binaire ci-dessous, recopier cet arbre et compléter cette numérotation.
<div class="centre">
```mermaid
    graph TD
    A["A : 1"] --> B["B : 10"]
    A --> C["C : 11"]
    B --> D["D : ..."]
    B --> E["E : 101"]
    C --> V1[" "]
    C --> F["F: ..."]
    D --> G["G: ..."]
    D --> H["H: ..."]
    F --> I["I: ..."]
    F --> V2[" "]
    style V1 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 4 stroke:#FFFFFF,stroke-width:0px
    style V2 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 9 stroke:#FFFFFF,stroke-width:0px
```
</div>

3. Justifier que sur un niveau donné de l'arbre tous les numéros de noeud ont le même nombre de caractères.
4. En déduire en fonction de $h$, le nombre de caractères formant le numéro des feuilles
5. En utilisant vos connaissances sur la numérotation binaire d'un entier positif, prouver que $n \leq 2^h - 1$.

{{ titre_activite("Implémentation des arbres binaires en Python",[])}}
Le notebook suivant présente une implémentation *possible* des arbres binaires en Python. Cette implémentation pourra être sauvegardée et utilisée en exercice.

{{ telecharger("Jupyter Notebook","./notebook/ArbresBinaires.ipynb")}}



## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("DOM",[],0) }}
On considère le code  {{sc("html")}} suivant :
```html
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Exemple</title>
</head>
<body>
    <h1> Un titre </h1>
    <p> Bonjour ! </p>
    <table>
        <tr>
            <td> Case 1</td>
            <td> Case 2</td>
        </tr>
    </table>
</body>
</html>
```
Ce document peut se représenter par un arbre :
```mermaid
    graph TD
    HTML["html"] --> HEAD["head"]
    HTML["html"] --> BODY["body"]
    HEAD --> META["meta"]
    HEAD --> TITLE["title"]
    BODY --> H1["h1"]
    BODY --> P["p"]
    BODY --> TABLE["table"] 
    TABLE --> TR["tr"]
    TR --> TD1["td"]
    TR --> TD2["td"]
```

1. Que représentent les noeuds de cet arbre ?
2. Que signifie du point de vue du {{sc("html")}} une arête de cet arbre ?
3. Quelle est la racine de cet arbre ?
4. Donner les feuilles de cet arbre.
5. Donner une branche de cet arbre.
6. Donner l'arité de cet arbre.
7. Donner la hauteur de cet arbre.

{{ exo("Vocabulaire sur les arbres",[]) }}

On considère l'arbre ci-dessous :
<div class="centre">
```mermaid
    graph TD
    A["A"] --> L["L"]
    A --> G["G"]
    L --> O["O"]
    L --> R["R"]
    G --> V1[" "]
    G --> I["I"]
    O --> T["T"]
    O --> H["H"]
    R --> M["M"]
    R --> E["E"]
    I --> S["S"]
    I --> V2[" "]
    style V1 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 4 stroke:#FFFFFF,stroke-width:0px
    style V2 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 11 stroke:#FFFFFF,stroke-width:0px
```
</div>

1. Justifier qu'il s'agit d'un arbre binaire. Quelle est sa taille ?
2. Quelle est sa racine ? Nommer les feuilles.
3. Donner une branche de cet arbre.
4. Donner la hauteur de cet arbre.
5. Donner une branche de longueur 3 dans cet 
6. On considère le sous arbre gauche de la racine, quel est l'arité de chaque noeud ? Que peut-on dire du sous arbre gauche ?
7. Même question pour le sous arbre droit de la racine.

{{ exo("Représenter un arbre binaire",[]) }}

1. Dessiner tous les arbres binaires à 3 noeuds. Attention à bien distinguer le fils droit du fils gauche.
2. Dessiner un arbre binaire de taille 4 et de profondeur 4.
3. Dessiner un arbre binaire de taille 4 et de profondeur 3.
4. Quelle est la taille maximale d'un arbre binaire de hauteur 10 ? Justifier 

    !!!aide 
        On pourra utiliser sans justification, la formule vue en cours qui permet d'encadrer la taille d'un arbre en fonction de sa hauteur.

{{ exo("Représenter un arbre binaire par un triplet",[]) }}
On rappelle qu'on peut définir un arbre binaire de façon récursive, en effet, un arbre binaire est soit vide (noté $\Delta$), soit un triplet $(etiquette,sag,sad)$ où $sag$ (pour sous arbre gauche) et $sad$ (pour sous arbre droit) sont eux-mêmes des arbres binaires. 

On considère les arbres suivants :

* $A = (7,\Delta,\Delta)$
* $B = (2,(3,\Delta,(9,\Delta,\Delta)),(10,\Delta,\Delta))$
* $C = (4,(1,(8,\Delta,\Delta),(7,\Delta,\Delta)),(3,(6,\Delta,\Delta),(5,\Delta,\Delta)))$

Pour chacun de ces arbres :

1. Faire un schéma pour le représenter.
2. Donner sa taille, sa hauteur, son nombre de feuilles.

{{ exo("Retour sur l'implémentation",[]) }}
On reprend ici l'implémentation des arbres binaires vu en cours que vous pouvez télécharger ci-dessous :
{{ telecharger("Implémentation arbres binaires","./files/C8/ab.py")}}

1. Compléter cette implémentation en écrivant une fonction `degenere(n)` qui prend en argument un entier positif `n` et qui renvoie l'arbre binaire dégénéré de taille `n`. On utilisera comme étiquette des noeuds `D0, D1, D2 ...`.
2. Compléter cette implémentation en écrivant une fonction `complet(h)` qui prend en argument en entier positif `h` et qui renvoie l'arbre binaire complet de hauteur `h`. On utilisera comme étiquette des noeuds `C0, C1, C2, ...`.
3. Reprendre ces deux fonctions et en écrire une version prenant aussi en paramètre une liste de chaines de caractères qui sera utilisée comme étiquette des noeuds. Par exemple `complet(2,["T","O","P"])` renvoie l'arbre binaire complet de hauteur 2 dont la racine porte l'étiquette `T` et a pour fils gauche `O` et fils droit `P`.
4. Utiliser ces deux fonctions de façons à créer rapidement l'arbre de l'exercice 2.
