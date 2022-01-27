def dec_to_bin(a):
    bin_a = str(a%2) #(1)
    a = a//2
    while a != 0 : #(2)
        bin_a = str(a%2) + bin_a #(3)
        a = a // 2
    return bin_a
