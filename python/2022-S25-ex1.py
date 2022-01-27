def selection_enclos(table_animaux,num_enclos):
    resultat = []
    for animal in table_animaux:
        if animal['enclos']==num_enclos:
            resultat.append(animal)
    return resultat