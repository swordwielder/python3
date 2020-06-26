# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    A=str(A)
    B=str(B)
    try:
        b = B.index(A)
        return b
    except:
        return -1
