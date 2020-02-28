s1 = 'sniper'


s2 = 'rpenis'


def testAna(s1,s2):

    if len(s1) != len(s2):
        return False

    letters ={}

    for i in s1:
        if i not in letters:
            letters[i]=1

        else:
            letters[i]+=1
    
    for i in s2:
            if i not in letters:
                return False

            else:
                letters[i]-=1

            if letters[i] == 0:
                del letters[i]

    return True

print(testAna(s1,s2))


def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        return True
    else: 
        return False

