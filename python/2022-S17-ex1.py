def nombre_de_mots(phrase):
    nb_espace = 0
    for caractere in phrase:
        if caractere==" ":
            nb_espace+=1
    if phrase[-1]==".":
        return nb_espace+1
    else:
        return nb_espace