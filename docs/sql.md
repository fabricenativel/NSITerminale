
{% set num = 2 %}
{% set titre = "Bases de données et SQL"%}
{% set theme = "db" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités  

{{ titre_activite("Un peu d'histoire et de théorie",["video"],0) }}

<div class="centre"><iframe width="560" height="315" src="https://www.youtube.com/embed/pqoIBiM2AvE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

En utilisant la vidéo ci-dessus et en faisant vos propres recherches sur le *Web*, répondre aux questions suivantes :

1. Quel mathématicien est à l'origine de la théorie des bases de données ? En quelle année ?
2. Avant l'avènement des bases de données, les données étaient stockés sous la forme de simples fichiers, quels étaient les inconvénients de ce fonctionnement ?
3. Que signifie l'*absence de redondance* pour une base de données ?
4. Que signifie l'*indépendance logique* pour une base de données ?
5. Que signifie l'*intégrité* pour une base de données ?
6. Donner les noms de quelques {{ sc("sgbd") }} connus en indiquant s'il s'agit de logiciels libres ou propriétaires.


{{ titre_activite("A la découverte de SQL",[]) }}


## Cours

{{ aff_cours(num) }}

## Exercices

{{ exo("Prix Nobel",[],0) }}
