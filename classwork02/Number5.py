with open("input.txt", "r") as f:
    s = f.read()
print(s[len(s)-1::-1])