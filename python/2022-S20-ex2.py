class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])
    
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])
    
    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)
        
    #test de la somme de chaque ligne
    for i in range(1,n): #(1)
        if carre.somme_ligne(i) != s:
            return False
        
    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s: #(2)
            return False
         
    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s: #(3)
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
    return True   #(4)
