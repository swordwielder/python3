from datetime import datetime
c,s=input().split()
format='%M:%S'
t=datetime.strptime(s,format)-datetime.strptime(c,format)
print(str(t)[3:])
