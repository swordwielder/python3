def alphanumeric(string):
    a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    b = list(string)
    return (any (item in b for item in a))

def alphabetical(string):
    a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    b = list(string)
    return (any(item in b for item in a))

def digits(string):
    a = ['1','2','3','4','5','6','7','8','9','0']
    b = list(string)
    return (any(item in b for item in a))

def lowercase(string):
    a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    b = list(string)
    return (any(item in b for item in a))

def uppercase(string):
    a=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    b = list(string)
    return (any(item in b for item in a))

if __name__ == '__main__':
    s = input()
    print (alphanumeric(s))
    print (alphabetical(s))
    print (digits(s))
    print (lowercase(s))
    print (uppercase(s))


