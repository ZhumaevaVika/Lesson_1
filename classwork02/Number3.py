n = int(input())

a = [[ max(i, j) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()