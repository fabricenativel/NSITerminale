1. Télécharger la base de données [lycees.db](./files/C2/lycees.db) qui contient une seule table `indicateurs` donnant les indicateurs de réussite au {{ sc("bac") }} des lycées français.
2. Lancer *DB Browser for sqlite* (depuis un terminale avec la commande `sqlitebrowser` ou via le menu des applications) et ouvrir la base de données téléchargée ci-dessus. Effectuer une sauvegarde dans le dossier de votre choix.
3. Instruction {{ sc("select") }} 
    1. Exécuter : 
        ```sql
             SELECT * FROM indicateurs;
        ```
        Vous obtenez comme résultat toute la table indicateurs, en effet `*` indique qu'on souhaite récupérer la totalité des champs de la table.
    
    2. Exécuter : 
        ```sql 
            SELECT etablissement, ville, academie FROM indicateurs;
        ```
        Cette fois vous n'obtenez que les champs indiqués (c'est à dire `etablissement`, `ville` et `académie`).   

4. Clause {{ sc("where") }}  
On peut bien sûr spécifier à l'aide de conditions les enregistrement que l'on souhaite récupérer :
    1. Exécuter : 
    ```sql
        SELECT * FROM indicateurs WHERE academie="LA REUNION";
    ```
    Quels enregistrements sont renvoyés ?
    2. Exécuter :
    ```sql
         SELECT * FROM indicateurs WHERE academie="LA REUNION" AND annee=2018
    ```
    Quels enregistrements sont renvoyés ?
    3. Ecrire une requête permettant d'afficher les lycées (etablissement, academie et ville) ayant présentés des candidats en hotellerie en 2018.

        !!! Aide
            * L'opérateur différent en SQL est `<>` il faudra donc préciser ici dans la clause `WHERE` que le champ 
            `effectif_presents_serie_hotellerie` doit être non nul.
            * Votre requête devrait renvoyer **70** enregistrements.

    4. Ecrire une requête permettant d'afficher les lycées (etablissement et ville) de l'académie de la Réunion ayant obtenu plus de 90 % de réussite toutes séries confondues en 2020.

        !!! Aide
            * Le champ concerné est `taux_brut_de_reussite_total_series`.
            * L'académie de la réunion est enregistré sous le nom "LA REUNION" dans la base de données
            * Votre requête devrait renvoyer 29 enregistrements.

    5. Exécuter : 

    ```sql
      SELECT etablissement FROM indicateurs WHERE etablissement LIKE "%BRASSENS%";
    ```

    1. Quels sont les enregistrements renvoyés ? En déduire le rôle de `LIKE` et du caractère `%`.
    2. Ecrire une requête permettant d'afficher les lycées (etablissement, ville) se situant dans une ville dont le nom se termine par `BES`.
    3. Ecrire une requête permettant d'afficher les lycées (etablissement, ville) se situant dans une ville dont le nom commence par `MAR`.

5. Clause `ORDER BY`

    Une requête SQL peut contenir une clause spécifiant l'ordre dans lequel les données sont affichées.

    1. Exécuter :
    
        ```sql
            SELECT etablissement, ville, taux_brut_de_reussite_total_series  FROM indicateurs WHERE academie="LA REUNION" and anne=2018 ORDER BY taux_brut_de_reussite_total_series;
        ```
    
        Les lycées sont alors classés par taux de réussite dans l'ordre *croissant* ({{ sc("asc") }}), on peut demander l'ordre décroissant en précisant {{ sc("desc") }} dans la requête :

        ```sql
            SELECT etablissement, ville, taux_brut_de_reussite_total_series  FROM indicateurs WHERE academie="LA REUNION"and anne=2018} ORDER BY\tt taux_brut_de_reussite_total_series.
        ```

    2. Ecrire une requête pour classer les villes présentes dans cette table en 2018 par ordre alphabétique croissant .

6. Clause `DISTINCT`

    1. Lors de l'exécution de la requête précédente, {{ sc("abbeville") }} apparaît deux fois au début, on peut préciser qu'un champ n'apparaît qu'une fois grâce à  `DISCTINCT`. 

    ```sql
      SELECT DISTINCT ville FROM indicateurs WHERE annee=2018 ORDER BY ville ASC
    ```
    
    2. Ecrire une requête pour classer les académies  par ordre alphabétique croissant, chaque académie ne doit apparaître qu'une fois.

6. Clause `LIMIT`
    
    1. Dans une requête, on peut spécifier grâce à une clause `LIMIT` le nombre maximum d'enregistrement à renvoyer. Exécuter :
    
    ```sql 
        SELECT etablissement, ville, effectif_presents_total_series FROM indicateurs WHERE annee=2018 ORDER BY effectif_presents_total_series} DESC LIMIT 20
    ```
    On limite ainsi le nombre d'enregistrement affichés à 20, ils sont classé par nombre de candidats au bac par ordre décroissant.
    
    2. Ecrire une requête permettant d'obtenir les 10 premiers lycées classés par nombre d'élèves de seconde en 2016.
    3. Ecrire une requête permettant d'afficher les 5 lycées de la Réunion ayant les moins bons taux de réussite au bac en 2017.

