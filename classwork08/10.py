def sredkvad(a, n):
    b = []
    for i in range(len(a)):
        b.append(0)
        if len(a)-1<=n:
            for j in range(i, i+n):
                b[i] = b[i] + a[j]**2
            b[i] = (b[i]/n)**0.5
        else:
            for j in range(i, len(a)):
                b[i] = b[i] + a[j]**2
            b[i] = (b[i]/(len(a)-i))**0.5
    print(b)
a = [1, 2, 3, 4, 5, 6, 7, 8]
sredkvad(a, 3)