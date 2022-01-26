def chercher(T,n,i,j):
    if i < 0 or j>len(T)-1: #(1)
        print("Erreur")
        return None    
    if i > j :
        return None
    m = (i+j) // 2 #(2)
    if T[m] < n :
        return chercher(T, n, m+1 , j) #(3) 
    elif T[m]>n :
        return chercher(T, n, i , m-1)
    else:
        return m 

