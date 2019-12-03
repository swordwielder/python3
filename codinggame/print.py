b = input()
s = ''
for a in b:
    a = ord(a)
    for i in range(48 if 47<a<58 else 65 if 64<a<91 else 97 if 96<a<123 else 0, a+1):
        s += chr(i)
print(s)
