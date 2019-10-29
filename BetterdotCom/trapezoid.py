#print("X value",X[i-1])
        #print(Y[i-1])
        #print("(Y[i]+Y[i-1])/2 = ",division)
        #print("total",total)
    
    #print("all total",alltotal)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y):
    # write your code in Python 3.6
    i=0
    division=0
    total=0
    alltotal=0
    for i in range(1,len(X)):
        division=(Y[i]+Y[i-1])/2
        total = division*(X[i]-X[i-1])
        alltotal = alltotal+total
        
    return alltotal

