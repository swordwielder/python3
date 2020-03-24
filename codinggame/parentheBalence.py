t=input()
def s(x):
 f='FALSE'
 t=[]
 for i in range(len(x)):
  if x[i] in '([{':t.append(x[i])
  elif x[i] in ')]}':
   if len(t)==0:return f
   p=t.pop()
   if x[i]==')' and p!='(':return f
   if x[i]==']' and p!='[':return f
   if x[i]=='}':
    if p!='{':return f
 if len(t)>0:return f
 return 'TRUE'
print(s(t))
