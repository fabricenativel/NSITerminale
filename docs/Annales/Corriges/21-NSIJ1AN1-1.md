{% set repere_sujet = "21-NSIJ1AN1" %}
{% set numero_exo = 1 %}

{{ correction_exobac(repere_sujet,numero_exo) }}

1.  a.  Cette requête affiche les champs et `salle` et `marque_ordi` de la table `Ordinateur`. 

    b.  Cette requête affiche les champs `salle` et `marque_ordi` de la table `Ordinateur` pour les enregistrement dont le champ `video` est à `true`

2. 
```sql
    SELECT * FROM Ordinateur WHERE annee>=2017 ORDER BY annee ASC
```

!!! note
    L'ordre croissant est l'ordre par défaut, on peut donc se passer du `ASC` dans la requête précédente. Pour mémoire l'ordre décroissant s'obtient avec `DESC`.

3.  a.  Une clé primaire est unique pour chaque enregistrement. Comme plusieurs ordinateurs peuvent être dans la même salle. Le champ salle n'est pas unique et ne peut donc pas servir de clé primaire.

    b. On souligne la clé primaire, on repère les clés étragères en les faisant précédées du symbole `#`.
    