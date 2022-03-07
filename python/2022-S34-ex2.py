def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) #(1)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0]) #(2)

def negatif(image):
    '''renvoie le negatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
# on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(nbCol(image)): #(3)
            L[i][j] = 255-image[i][j] #(4)
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inferieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(nbCol(image)): 
            if image[i][j] < seuil : #(5)
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
