def rendu(somme_a_rendre):
    n1 = somme_a_rendre//5
    somme_a_rendre = somme_a_rendre%5
    n2 = somme_a_rendre//2
    n3 = somme_a_rendre%2
    return [n1,n2,n3]
