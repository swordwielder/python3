n = int(input())
scr = input().lower()
a= sorted(scr)
for i in range(n):
    acc = input()
    if a==sorted(acc.lower()):
        print(acc)
