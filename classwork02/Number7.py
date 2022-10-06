with open('input4.txt', 'r', encoding='utf-8') as f:
    ball = 0
    a = []
    for line in (f.readlines()):
        if ball<int(line.split()[3]):
            ball = int(line.split()[3])
with open('input4.txt', 'r', encoding='utf-8') as f:
    for line in (f.readlines()):
        if int(line.split()[3]) == ball:
            a.append(int(line.split()[2]))
a.sort()
for i in range (len(a)-2):
    if a[i]==a[i+1]:
        a.pop(i)
print(*a)