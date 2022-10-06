d = {'9':0, '10':0, '11':0}
with open('input2.txt', 'r', encoding='utf-8') as f:
    for line in (f.readlines()):
        klass = line.split()[2]
        ball = line.split()[3]
        if d[klass] < int(ball):
            d[klass] = int(ball)
    for i in d:
        print(d[i], end = ' ')