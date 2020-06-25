# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num = 1
    A.sort()
    if 1 not in A:
        return 1
    if A[len(A)-1] < 1:
        return 1
    else:
        for i in range(len(A)):
            if A[i] == num+1:
                num+=1
            elif A[i] > num+1:
                return num+1
        return num+1


def solution2(a):
    # write your code in Python 3.6
    A = set(a)
    ans = 1
    while ans in A:
       ans += 1
    return ans

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution3(A):
    seen = set()
    for i in A:
        seen.add(i)
        
    ret = 1
    while True:
        if ret in seen:
            ret += 1
        else:
            return ret
    
        


if __name__ == '__main__':
    b = [1,3,6,4,1,2]

    a = set(b)
    c = map(b)
    print ("set of b is ",a)
    print ("map of b is ", c)
    print ("smallest integer value", solution(b))
