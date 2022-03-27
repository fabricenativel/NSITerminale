
{% set num = 13 %}
{% set theme = "algorithmique" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Recherche simple",[],0) }}

1. Fonctions natives de Python
    1. Consulter la [documentation de Python sur la méthode `find` des chaînes de caractères](https://docs.python.org/fr/3/){target=_blank}.

    2. Quel est le rôle de cette méthode ?

    3. Tester cette méthode sur les exemples suivants, (dans un notebook ou dans une console Python) :

        1. `'numérique et sciences informatiques'.find('que')`
        2. `'numérique et sciences informatiques'.find('nsi')`


        !!! note
            Une autre méthode presque identique ([`str.index`](https://docs.python.org/fr/3/library/stdtypes.html?highlight=str%20index#str.index){target=_blank}) lève une erreur lorsque le motif cherché ne se trouve pas dans la chaîne.

2. Visualisation d'un algorithme "naïf"

    Un [outil en ligne](https://boyer-moore.codekodo.net/recherche_naive.php){target=_blank} (mise en ligne par L. Abdal, d'après un travail de N. Reveret), permet de visualiser un algorithme dit de "recherche naïve". Utiliser cette outil (en variant éventuellement le motif et la chaîne). Puis expliquer en quelques mots le principe de cet algorithme de recherche.  
        [Visualisation algorithme naïf :octicons-link-external-24:](https://boyer-moore.codekodo.net/recherche_naive.php){ .md-button target=_blank}

2. Ecrire ses propres fonctions
    1. Sans utiliser `find` ou `index`, écrire une fonction `recherche(motif,chaine)` qui renvoie `True` ou `False` suivant que
    la chaîne de caractères `motif` se trouve ou non dans `chaine`.
    2. Même question mais en renvoyant l'indice de la première position de `motif` dans `chaine` (si elle s'y trouve) et `-1` sinon.

{{ titre_activite("Amélioration de la recherche simple",[]) }}

1. Le même [outil en ligne](https://boyer-moore.codekodo.net/recherche_boyer.php){target=_blank} que dans l'activité précédente permet de visualiser un second algorithme plus performant . Utiliser cette outil (en variant éventuellement le motif et la chaîne). 
        [Visualisation algorithme Boyer-Moore :octicons-link-external-24:](https://boyer-moore.codekodo.net/recherche_boyer.php){ .md-button target=_blank}

    !!! aide
        On pourra remarquer que :

        *  La comparaison commence par la *fin* du motif
        *  On a construit un tableau indiquant pour chaque caractère du motif sa dernière occurrence dans le motif
        *  Par rapport à une recherche naïve, on peut parfois décaler  le motif de plusieurs emplacements

2. Décrire en quelques phrases le principe de ce nouvel algorithme de recherche.  

!!! note
    L'algorithme présenté dans cette activité est une version simplifiée de l'algorithme de Boyer-Moore par Horspool. L'algorithme complet, plus complexe n'est pas étudié en {{ sc("nsi")}}. L'élève intéressé pourra consulter les ressources en ligne (par exemple [la page wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm){target=_blank})


## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("Nombre de comparaisons dans la recherche simple",[],0) }}

1. Lors d'une recherche naïve, combien de comparaisons sont effectuées pour la recherche du motif `info` dans la chaine de caractères `numérique et sciences informatiques` ?

2. On donne ci-dessous l'implémentation vue en cours d'une recherche naïve :
```python
def recherche(motif,chaine):
    lm,lc = len(motif),len(chaine)
    for i in range(lc-lm+1):
        i_motif,i_chaine = 0,i
        while i_motif<lm and chaine[i_chaine] == motif[i_motif]:
            i_motif += 1
            i_chaine += 1
        if i_motif == lm:
            return True
    return False
```

    a. Modifier cette fonction afin qu'elle renvoie en plus du booléen, le nombre de comparaisons  effectuées.

    b. Tester cette nouvelle fonction afin de retrouver le résultat de la question 1.

    c. Rappeler le nombre de comparaisons maximales effectuées pour cherche un motif de longueur $l_m$ dans une chaine de longueur $l_c$.

    d. Combien de comparaisons sont nécessaires pour recherche le motif `aaaaaaaaab` dans une chaine contenant dix mille `a` ?

    !!! aide
        On rappelle qu'en python `"a"*10000` est la chaine de caractères constituée de dix mille fois le caractère `a`.


{{ exo("Indice du motif",[]) }}

1. Modifier la fonction de recherche naïve vue en cours (et donnée dans l'exercice précédent) de façon à ce qu'elle renvoie l'indice de la première occurrence du motif dans la chaine s'il est présent et $-1$ sinon.
2. Même question avec l'indice de la dernière occurrence.
3. Modifier de nouveau cette fonction pour qu'elle renvoie la liste des indices des occurrences du motif dans la chaine. Par exemple `recherche("ici","ici, ou encore ici ou même là")` renvoie la liste `[0,15]`.

{{ exo("Implémentation de l'accélération",[]) }}

1. Ecrire une fonction `traite` tel que `traite(motif)` renvoie un dictionnaire contenant pour chaque caractère du motif, l'indice de sa dernière position dans le motif. Par exemple : `traite("extra")` renvoie `{'e': 0, 'x': 1, 't': 2, 'r': 3, 'a': 4}` et  `traite("exemple")` renvoie `{'e': 6, 'x': 1, 'm': 3, 'p': 4, 'l': 5}`

2. En utilisant cette fonction, proposer une implémentation de l'algorithme d'accélération vue en cours.
