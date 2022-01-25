def recherche(liste):
    consecutifs = []
    for i in range(len(liste)-1):
        if liste[i+1]==liste[i]+1:
            consecutifs.append((liste[i],liste[i+1]))
    return consecutifs


