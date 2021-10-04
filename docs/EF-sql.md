# Evaluation de NSI du 05/10/2021

!!! danger "Attention"
    * Répondre sur un document *libreoffice writer*
    * Enregistrer ce document dans votre dossier personnel dans `Evaluations/DS3/`


## Exercice 1

Un collectionneur de disque vinyl  souhaite créer une base de données des morceaux de musique qu'il possède. Cette base serait composée d'une seule table :
    <table>
        <tr><th colspan="2" align="center"> Vinyl </th></tr>
        <tr><td>`Titre`</td><td>`TEXT`</td></tr>
        <tr><td>`Auteur`</td><td>`INTEGER`</td></tr>
        <tr><td>`Année`</td><td>`INTEGER`</td></tr>
        <tr><td>`Catégorie`</td><td>`INTEGER`</td></tr>
    </table>

1. Quels sont les attributs de cette table ?
2. On souhaite ajouter un attribut `Durée` qui indique la durée du morceau de musique, proposer un type pour cette attribut.
3. Proposer un domaine pour l'attribut `Année`.
4. Expliquer dans quelle situation le **principe d'unicité** des bases de données n'est pas respectée avec cette table. Que faire pour y remedier ?


## Exercice 2

{{ exo("Pays du monde",[]) }} 

#### Préambule
1. Télécharger ci-dessous une base de données des pays du monde :
{{telecharger("Pays","./files/C2/countries.db")}}
2. Ouvrir cette base avec `sqlitebrowser`
3. Dans <span class='encadre'>Parcourir les données</span> prendre note du noms des colonnes. 

    !!! Note
        On précise la signification des champs suivants ainsi que leur type :
        
        * `Population` : le nombre d'habitants (type entier)
        * `Region` : la région (en anglais) dans laquelle se trouve le pays (type texte). Par exemple la France se trouve en {{sc("western europe")}}
        * `Area` : la surface du pays (en *mile* carré)  (type entier)
        * `Coastline` : la surface côtière du pays (type réel), cette valeur vaut `0.0` lorsque le pays n'a pas d'ouverture sur la mer.
        * `GDP` : le produit intérieur brut par habitant (type entier). C'est une mesure de la richesse du pays.

#### Requêtes SQL
Dans chaque cas, répondre en **écrivant une requête {{sc("sql")}}** dont on donnera les résultats :

1. Donner la population et le produit intérieur brut de l'Allemagne (*Germany* en anglais)

    !!! Aide
        Le modèle de réponse attendue est donc : <BR>
        *"La population de l'Allemagne est ..... et son {{sc("pib")}} est .... <br>
        Résultats obtenus avec la requête .................................... "*

2. Combien de régions différentes pour les pays figurent dans cette base de données ?
3. Lister par ordre croissant les trois pays les plus peuplés au monde.
4. Donner les noms des pays commençant par un `t` et finissant par `istan`.
5. Donner le plus grand pays (en surface) n'ayant pas d'ouverture sur la mer.

#### Recherches d'informations
En argumentant vos réponses à l'aide d'informations extraites de ces données, donner votre opinion sur les affirmations suivantes :

1. Les pays les plus riches sont souvent aussi les plus grands (en surface).
2. L'europe de l'ouest est la région la plus riche de la planète.

## Exercice 3

1. En consultant cette [page wikipedia](https://fr.wikipedia.org/wiki/Loi_de_Benford){target=_blank}, ou en faisant vos propres recherches sur le *Web*, expliquer rapidement ce qu'est la **loi de Benford**
2. Les populations des pays de la base de données de l'exercice précédent suivent-elles la loi de Benford ?

    !!! Aide
        Bien que le champ `population` soit de type entier, on peut utiliser `LIKE` comme sur une chaine de caractère pour extraire les pays dont la population commence par un 1 et les compter.
