import textwrap

def wrap(string, max_width):
    new = ""
    for a in range(len(string)):
        if a!=0:
            if a%max_width==0:
                new+="\n"
        new+=string[a]

    return new

    

    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
