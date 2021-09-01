
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

    def __strt__(self):
        return f"{self.heures}h {self.minutes}m {self.secondes}s"
```

    1. Quelle classe est crée ? Quels sont les attributs des objets de cette classe ?
    2. Quelle méthode est crée pour les objets de cette classe ?

2. Le record du monde du marathon est actuellement de deux heures, une minute et trente neuf secondes, créer à l'aide de la classe ci-dessus un objet `record_marathon` représentant cette durée et l'afficher.

{{ titre_activite("Calcul fractionnaire",[]) }}
{{ telecharger("Fiche d'activité","./notebook/IntroPOO.ipynb")}}
## Cours

{{ aff_cours(num) }}




## Exercices

{{ exo("Définir et instancier une classe",[],0) }}

