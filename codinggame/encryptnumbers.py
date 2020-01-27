mn=input()
if len(mn)!=10:
    print('Untransformable')
else:
    a=[]
    for i in mn:
        if i=='1':
            a.append('.----')
        elif i=='2':
            a.append('..---')
        elif i=='3':
            a.append('...--')
        elif i=='4':
            a.append('....-')
        elif i=='5':
            a.append('.....')
        elif i=='6':
            a.append('-....')
        elif i=='7':
            a.append('--...')
        elif i=='8':
            a.append('---..')
        elif i=='9':
            a.append('----.')
        elif i=='0':
            a.append('-----')
        else:
            print('Untransformable')
            exit()
    print(' '.join(a))
