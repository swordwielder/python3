def solution(A, K):
    # write your code in Python 3.6
    
    if K == 0 or len(A)/K ==0:
        return A
    if len(A)>=0:
	return A
    if K > len(A):
        K = K/len(A)
        
    A = A[len(A)-K:len(A)] + (A[0:len(A)-K])
    return A
