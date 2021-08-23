
{% set num = 3 %}
{% set theme = "os" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("TITRE_ACTIVITE_1",[],0) }}


CONTENU ACTIVITE 1

{{ titre_activite("TITRE_ACTIVITE_2",[]) }}


CONTENU ACTIVITE 2

...

## Cours

{{ aff_cours(num) }}




## Exercices

{{ exo("TITRE_EXO_1",[],0) }}


CONTENU EXO 1


{{ exo("TITRE_EXO_2",[]) }}


CONTENU EXO 2


{{ exo("TITRE_EXO_3",[]) }}


CONTENU EXO 3