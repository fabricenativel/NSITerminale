
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

2. Ecrire ses propres fonctions
    1. Sans utiliser `find` ou `index`, écrire une fonction `recherche(motif,chaine)` qui renvoie `True` ou `False` suivant que
    la chaîne de caractères `motif` se trouve ou non dans `chaine`.
    2. Même question mais en renvoyant l'indice de la première position de `motif` dans `chaine` (si elle s'y trouve) et `-1` sinon.

{{ titre_activite("Amélioration de la recherche simple",[],0) }}




## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("....",[],0) }}

