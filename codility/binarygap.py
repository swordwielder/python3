# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
import os
def solution(N):
    # write your code in Python 3.6
    binarygap=0
    count=0

    a = bin(N).replace("0b", "")
    if len(a) < 3:
        return 0
    print(a)
    for i in range(len(a)):
        if a[i] =='1':
            b=a[i+1:]
            j=0
            for i in b:
                if i == '1':
                    if binarygap < count:
                        binarygap=count
                    count=0
                    break
                else:
                    count+=1

    return binarygap

if __name__ == '__main__':
    print(solution(74901729))
