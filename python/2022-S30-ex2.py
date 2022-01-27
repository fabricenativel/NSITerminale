def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} #(1)
    if len(nombre) == 1:
        return dico[nombre] #(2)

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
		 ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
    
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre_droite) #(3)
        else:
            return rom_to_dec(nombre_droite)-dico[nombre[0]] #(4)
