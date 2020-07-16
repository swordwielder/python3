r = int(input())
g = int(input())
b = int(input())
t='#'
if len(hex(r)[2:]) <2:
    t+='0'
t+=hex(r)[2:].upper()
if len(hex(g)[2:])<2:
    t+='0'
t+=hex(g)[2:].upper()
if len(hex(b)[2:])<2:
    t+='0'
t+=hex(b)[2:].upper()
print(t)
