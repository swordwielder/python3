    name = []
    spaces = []
    name = s.split()
    print ("first")
    for i in s:
        print (i)
    print ("second")
    for i in range(0,len(s)):
        if s[i] == " ":
            print(i)
    capname = ""
    for i in name:
        #print (i)
        capname+=i.capitalize()+" "
    return capname
