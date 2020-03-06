n=int(input())
x=input()
print(''.join(chr((ord(i)-97+n*len(x))%26+97) if i.isalpha() else i for i in x))
