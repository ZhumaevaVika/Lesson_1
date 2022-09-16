s = list(map(str, input().split()))
x = set(s[0])
for word in s:
    x = x&set(word)
print(x)