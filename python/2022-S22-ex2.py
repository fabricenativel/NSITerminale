def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N): 
        if tab[i] == True: #(1)
            premiers.append(i)
            for multiple in range(2*i, N, i): #(2)
                tab[multiple] = False #(3)
    return premiers
