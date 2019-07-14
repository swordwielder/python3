def swap_case(s):
    a = s.swapcase()
    return a

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#long solution not mine
def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a

