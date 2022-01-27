def fibonacci(n):
    d = {1 : 1, 2 : 1}
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]
