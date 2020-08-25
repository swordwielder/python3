text = input()
moves = input()
for i in moves:
    if i=='>':
        text=text[-1:]+text[:-1]
    else:
        text=text[1:]+text[0]
print(text)

#https://www.codingame.com/clashofcode/clash/report/135214045004b99e669933bd5fc40d83bf98710
