
{% set num = 14 %}
{% set theme = "python" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Programme comme donnée",[],0) }}

De façon schématique, un programme (ou une fonction) prend en entrée des **données**, effectue un traitement sur ces données et produit un résultat :

<div class="centre">
        ```mermaid
        graph LR
        D["Données"]
        P(["&#9881; Programmes"])
        R["Résultat"]
        D --> P
        P --> R
        ```
</div>

1. Dans l'exemple d'une fonction qui compte le nombre de lettres dans un mot, que sont les données ? le résultat ?

2. On souhaite écrire une fonction qui compte le nombre de lignes d'un fichier. Que sont les données de cette fonction ?

3. Que sont les données pour les programme suivants : un antivirus, un compilateur ?

4. Recopier et compléter avec les mots "*programme*" et "*donnée*" : 

    > un ........ prend des ....... en entrée mais, un ........ peut aussi être la ............ d'un .............


{{ titre_activite("Problème de l'arrêt",[]) }}

On suppose qu'on dispose d'un programme appelé `teste_arret` qui prend en entrée un programme `P` et des données `X` et renvoie `True` ou  `False` selon que `P` s'arrête ou non avec les données `X` comme cela est schématisé ci-dessous :
<div class="centre">
        ```mermaid
        graph LR
        D["Programme P"]
        X["Données X"]
        P(["&#9881; teste_arret"])
        T["True"]
        F["False"]
        D --> P
        X --> P
        P --P s'arrête avec les données X--> T
        P --P ne s'arrête pas avec les données X--> F
        ```
</div>

1. On définit le nouveau programme suivant :

    ```python linenums="1"
    def Q(P,X):
        if teste_arret(P,X):
            while True:
                pass
        else:
            return 1
    ```

    1. Que dire des lignes 3 et 4 (on rappelle que l'instruction `pass` ne fait rien)
    2. Si `P` s'arrête avec les données `X`, que fait ce programme ?
    3. Si `P` ne s'arrête pas avec les données `X`, que fait ce programme ?

2. Le programme `Q` prend en entrée un programme `P` et des données X, il peut donc se prendre lui-même en entrée avec lui-même comme donnée ! On cherche  à déterminer le résultat de l'appel : `Q(Q,Q)`. Pour cela, recopier et compléter le schéma suivant :

    <div class="centre">
        ```mermaid
        graph LR
        D["Programme : ..."]
        X["Données : ..."]
        P(["&#9881; Programme Q"])
        T["...."]
        F["Arrêt"]
        D --> P
        X --> P
        P --Q ...... avec Q comme donnée--> T
        P --Q ne s'arrête pas avec Q comme donnée X--> F
        ```
</div>

3. D'après ce schéma, que se passe-t-il si `Q` s'arrête avec lui même comme donnée ? Et dans le cas contraire ? Que peut-on en conclure sur l'existence du programme `teste_arret` ?

!!! note
    On pourra compléter cette activité avec le visionnage de la vidéo suivante :
    <div class="centre">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/92WHN-pAFCs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

Dans cette activité, nous avons prouvé que le programme `teste_arret` ne peut pas exister, on dit que le problème de l'arrêt est **indécidable** c'est à dire qu'il n'existe pas d'algorithme permettant de résoudre ce problème. 

## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("Vocabulaire",[],0) }}

1. Donner un ou plusieurs exemples de programmes acceptant un programme comme donnée 
2. Donner un exemple de fonction calculable.
3. Donner un exemple de problème indécidable.
4. Que signifie la phrase *"le problème de l'arrêt est indécidable"* ?

{{ exo("Nombre premier",[]) }}

1. Proproser un algorithme permettant de savoir si un entier donné $n$ est premier ou non. Que peut-on en déduire sur la décidabilité de ce problème ?
2. Implémenter en Python cet algorithme.
