text = input()
moves = input()
for i in moves:
    if i=='>':
        text=text[-1:]+text[:-1]
    else:
        text=text[1:]+text[0]
print(text)

