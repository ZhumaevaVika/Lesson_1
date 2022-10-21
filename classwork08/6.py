A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

A = set(A)
B = set(B)
C = set(C)
D = set(D)

print((A&D)|(C&B))