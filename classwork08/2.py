s = str(input())
count = 0
for letter in s:
    if 47<ord(letter)<58:
        count += 1
print(count)