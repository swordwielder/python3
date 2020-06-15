
text = input()
alpha =string.ascii_lowercase*10


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
res =''

for i in range(len(text)):
    if text[i].isalpha():
        if text[i].islower():
            alIndex = alpha.index(text[i])
            res+=alpha[alIndex+i]
        else:
            alIndex = alpha.index(text[i].lower())
            res+=alpha[alIndex+i].upper()
    else:
        res+= text[i]
print(res)
