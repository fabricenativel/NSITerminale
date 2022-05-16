
def genere_cle(mot,n):
    nb_fois = n//len(mot)
    reste = n%len(mot)
    cle = nb_fois * mot
    for i in range(reste):
        cle += mot[i]
    return cle


print(genere_cle("YAK",8))
