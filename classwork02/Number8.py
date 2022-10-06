f = open('input3.txt', 'r', encoding='utf-8')
a = []
for line in f:
    line = line.split()
    line.pop(2)
    a.append(line)
f.close()
a.sort()
for i in a:
    for j in i:
        print(j, end=' ')
    print()