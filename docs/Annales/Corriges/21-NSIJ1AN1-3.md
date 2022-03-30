{% set repere_sujet = "21-NSIJ1AN1" %}
{% set numero_exo = 3 %}

{{ correction_exobac(repere_sujet,numero_exo) }}

1.  

    a.  
    ```python
    def total_hors_reduction(tab):
        '''Calcul la somme des éléments de tab'''
        assert type(tab)==list, "L'argument doit être une liste"
        thr = 0
        for prix in tab:
            assert type(prix)==int or type(prix)==float,"Les prix doivent être de types numériques"
            thr += prix
        return thr
    ```

    b.
    ```python
    def offre_bienvenue(tab):
        """ tableau -> float """
        somme =0
        longueur = len(tab)
        if longueur > 0:
            somme = tab[0]* 0,8
        if longueur > 1:
            somme = somme + tab[1] * 0,7
        if longueur > 2:
            for i in range(2,longueur):
                somme = somme + tab[i]
        return somme
    ```

2.  
```python
def prix_solde(tab):
    if len(tab)>=5:
        return total_hors_reduction(tab)*0.5
    elif len(tab)==4:
        return total_hors_reduction(tab)*0.6
    elif len(tab)==3:
        return total_hors_reduction(tab)*0.7
    elif len(tab)==2:
        return total_hors_reduction(tab)*0.8
    else:
        return total_hors_reduction(tab)*0.9
```

3.  

    a.  
    ```python
    def minimum(tab):
        min_courant = tab[0]
        for elt in tab:
            if elt<min_courant:
                min_courant = elt
        return min_courant
    ```

    b.  
    ```python
    def offre_bon_client(tab):
        if len(tab)>=2:
            return total_hors_reduction(tab)-minimum(tab)
        else:
            return total_hors_reduction(tab)
    ```

4. a.  
    ```python
    tab = [35.0,30.5,20.0,15.0,10.5,5.0,6.0]
    ```

    Le total des prix du panier est de $35 + 30,5 + 20 + 15 + 10.5 + 6 + 5=122$. Compte tenu de l'ordre des articles les articles coutant 20 € et 5 € seront offerts. Et donc le prix à payer sera 97 €.

    b.  
    ```python
    tab = [35.0,30.5,20.0,15.0,10.5,6.0,5.0]
    ```
    Le prix total a payer est de 96 euros.

    c.
    Il faut trier les objets par ordre décroissant de prix.
