w = input()
last = ord(w[0])-65
for c in w[1:]:
    if(ord(c)-65<last):
        print(c)
        break
    last = ord(c)-65
