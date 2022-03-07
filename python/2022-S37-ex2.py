urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

def depouille(urne):
    resultat = {} #(1)
    for bulletin in urne:
        if bulletin in resultat: #(2)
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : #(3)
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax] #(4)
    return liste_finale