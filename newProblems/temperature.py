for i in range(int(input())):
 b,t=map(int,input().split())
 f=(b-32)*5/9
 if f>t:print('Higher')
 elif f<t:print('Lower')
 else:print('Same')
