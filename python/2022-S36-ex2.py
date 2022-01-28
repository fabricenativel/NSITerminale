from math import sqrt   # import de la fonction racine carree

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) #(1)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus     
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point,depart) #(2)
    for i in range (1, len(tab)): #(3)
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i],depart)
    return point

