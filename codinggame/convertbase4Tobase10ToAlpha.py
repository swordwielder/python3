n = int(input())
for i in range(n):
    password = input()
    b=[]
    for i in range(0,len(password),4):
        b.append(chr(int(password[i:i+4],4)))
    print("".join(b))
