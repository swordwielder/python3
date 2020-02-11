y=int(input())
print(str((y%4<1 and(y%100>0 or y%400<1))).lower())


y=int(input())
if y%4==0:
   if y%100==0:
       if y%400==0:print("true")
       else:print("false")
   else:print("true")
else:print("false")
