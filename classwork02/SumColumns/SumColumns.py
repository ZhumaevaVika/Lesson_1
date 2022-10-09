import itertools as it

with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: [int(y) for y in x.rstrip().split()], a))
#print(a)

rez = it.zip_longest(*a, fillvalue=0)
k = []
for i in list(rez):
    s = sum(list(i))
    k.append(str(s))
print(*k)
with open("output.txt", "w") as f:
    f.writelines([word + ' ' for word in k])