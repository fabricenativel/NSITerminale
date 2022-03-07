class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None



def expression_infixe(e):
    s = "" #(1)
    if e.gauche is not None: #(2)
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None: #(3)
        s = s + expression_infixe(e.droit) + ')'
    if True : #(4)
        return s
