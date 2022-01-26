def binaire(a):
    bin_a = str(a%2) #(1)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a #(2)
        a = a//2 #(3)
    return bin_a