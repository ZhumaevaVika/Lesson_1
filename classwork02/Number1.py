n, m = map(int, input().split())
t = 0
a = [[ j+(i*n)+i for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()