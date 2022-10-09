import itertools as it
with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: [str(y) for y in x.rstrip().split()], a))
n = int(a[0][0])
a = a[1:]
print(n, a)
sequence = it.count(start=0, step=1)
element = next(sequence)
el = []
while(element <= len(a)-1):
    el.append(element)
    element = next(sequence)
print(*el)
print(a)
a2 = []
for j in a:
    strok = ''
    for word in j:
        strok += word + ' '
    a2.append(strok)
print(a2)
with open("output.txt", "w") as f:
    f.writelines([str(i%n) + ' ' + a2[i] + '\n' for i in el])