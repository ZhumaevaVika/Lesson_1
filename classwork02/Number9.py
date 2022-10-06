klass9 = []
klass10 = []
klass11 = []
with open('input2.txt', 'r', encoding='utf-8') as f:
    for line in (f.readlines()):
        klass = line.split()[2]
        ball = line.split()[3]
        if int(klass) == 9:
            klass9.append(int(ball))
        elif int(klass) == 10:
            klass10.append(int(ball))
        else:
            klass11.append(int(ball))
print(sum(klass9)/len(klass9), sum(klass10)/len(klass10), sum(klass11)/len(klass11), end=' ')