def pascal(n):
    C= [[1]] #(1)
    for k in range(1,n+1):
        Ck = [1] #(2)
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] ) #(3)
        Ck.append(1) #(2)
        C.append(Ck)
    return C
