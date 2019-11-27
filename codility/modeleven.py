def solution(A):
    # write your code in Python 3.6
    a = float("inf")
    for i in A:
        if i%11==0 and i < a:
            a=i
    return a
