# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import product

def cartesian(a,b):
    for i in a:
        for j in b:
            print ( "("+str(i)+", "+str(j)+") ", end='')#='', flush=True)


if __name__ == '__main__':
    
    a=map(int,raw_input().split())
    b=map(int,raw_input().split())
    #a = int(input().split())
    
    #print("printing a")
    #print(a)
    #print("printing b")
    #print(b)
    cartesian(a,b)
