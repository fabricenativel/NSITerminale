def tri_bulles(T):
    n = len(T) 
    for i in range(len(T)-1,0,-1): #(1)
        for j in range(i):
            if T[j] > T[j+1]: #(2)
                temp = T[j] #(3)
                T[j] = T[j+1] 
                T[j+1] = temp
    return T

