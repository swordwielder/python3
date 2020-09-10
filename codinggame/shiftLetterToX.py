shift = int(input())
plaintext = input()
r=''
for i in plaintext:
    if i.isalpha():
        if ord(i)-shift<65:
            r+=chr(ord(i)-shift+26)
        else:
            r+=chr(ord(i)-shift)
    else:
        r+=i
print(r)
