# Evaluation de NSI du 20/09/2021

!!! danger "Attention"
    Tous les programmes demandés doivent être enregistrés dans votre dossier personnel dans `Evaluations/DS2/`


## Exercice 1

On donne ci-dessous le squelette d'un programme Python utilisant le module `turtle` qui pourra être utilisé pour répondre aux questions de l'exercice.
```python
import turtle

# Création du "papier" et du "crayon"
crayon = turtle.Turtle()
papier = turtle.Screen()

# Taille, dimension et couleur pour le papier et le crayon
papier.bgcolor("beige")
papier.setup(width=500,height=500)
crayon.color("navy")
crayon.pensize(5)


# Attends un clic pour fermer la fenêtre de dessin
papier.exitonclick()
``` 


1. Ecrire un programme Python **itératif** permettant de dessiner la frise suivante :
![Frise](./images/Eval/frise.png){: .imgcentre}
Le repère et les graduations sont là pour vous aider et ne doivent pas être reproduits.
2. On considère qu'une frise est constituée d'un motif de base et d'une frise ayant un motif de moins. En utilisant cette définition récursive de la frise, écrire un programme **récursif** permettant de la dessiner.
    

## Exercice 2

On s'intéresse à un algorithme **récursif** de rendu de monnaie. On veut donc écrire une fonction récursive `rendu(somme,systeme_monetaire)` qui renvoie la liste des pièces du `systeme_monetaire` permettant de former `somme`. On suppose aussi que la liste des valeurs du système monétaire est donné par **ordre décroissant** de valeurs. 

Par exemples :

```python
>>> rendu_monnaie(67,[50,20,10,5,2,1])
[2, 5, 10, 50]
>>> rendu_monnaie(143,[50,20,10,5,2,1])
[1, 2, 20, 20, 50, 50]
```

!!! Rappel
    On rappelle qu'il s'agit d'un algorithme glouton. Dans cet exercice, pour simplifier, on considère que le système monétaire utilisé est canonique et que donc cet algorithme n'échoue pas.


Compléter le code Python suivant :

```python
def rendu_monnaie(somme,systeme_monetaire):
    ''' Renvoie la liste des pieces de systeme_monetaire permettant de former  somme'''
    # Cas de base, la somme à rendre est nulle
    if .............:
        return []
    else:
    # Appel récursif selon que la pièce de plus grande valeur (forcément situé en début de systeme_monetaire) est utilisée ou non
        piece = .............
        if .............:
            # piece utilisée, l'ajouter à liste qu'on renvoie et la soustraire de la somme
            return rendu_monnaie(.........,...........)+[piece]
        else:
            # pièce non utilisée car de trop grande valeur, la supprimer du système monétaire
            systeme_monetaire.....(0)
            return rendu_monnaie(......,.........)
```

**Bonus** (à faire uniquement s'il vous reste du temps) :

1. Ajouter les instructions `assert` permettant de vérifier les préconditions sur les arguments
2. Traiter le cas des systèmes monétaires non canoniques  en renvoyant la liste vide lorsque l'algorithme échoue à trouver une solution. A titre d'exemple, `rendu_monnaie(11,[10,8,3])` admet une solution `[8,3]` mais l'algorithme glouton échoue et devra donc renvoyer `[]`.