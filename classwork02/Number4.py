with open('input.txt') as f:
    for text in reversed(f.readlines()):
        print(text, end='')