n, m = map(int, input().split())

a = [[ (2-int(i<j))*int((i!=j)) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()