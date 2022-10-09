import codecs
import collections
n = int(input())

with codecs.open('input.txt', encoding='utf-8') as f:
    a = f.readlines()
    a = list(map(lambda x: [str(y) for y in x.rstrip().split()], a))
#print(a)

a2 = []
for line in a:
    for word in line:
        a2.append(word.lower())
#print(a2)

cnt = collections.Counter()
for word in a2:
    cnt[word] += 1
#print(cnt)
cnt2 = {k: v for k, v in sorted(cnt.items(), key=lambda item: item[-1], reverse=True)}
#print(cnt2.values())
#print(list(cnt.items()))
for key, value in list(cnt2.items())[:n]:
    print(key, end = ' ')

