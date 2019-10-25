def solution(a):
    # write your code in Python 3.6
    A = set(a)
    ans = 1
    while ans in A:
       ans += 1
    return ans


if __name__ == '__main__':
    b = [1,3,6,4,1,2]

    a = set(b)
    c = map(b)
    print ("set of b is ",a)
    print ("map of b is ", c)
    print ("smallest integer value", solution(b))
