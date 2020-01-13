# a=[-2,1,-3,4,-1,2,1,-5,4]
# return the indexes with the most sums

def solution3(x):
    left=0
    right=0
    runsum=x[0]
    best=x[0]
    a=[0,0]
    while left<right:
        if runsum>best:
            best = runsum
            a=[]
            print("x left is ",x[left])
            print("x right is ",x[right])
            a.append(left)
            a.append(right)
            left+=1
        print("x left is ",x[left])
        print("x right is ",x[right])
        right+=1
        runsum +=x[right]
        if right==len(x):
            break
    #print(x)
    return a


def solution2(x):
    left=0
    right=0
    runsum=x[0]
    best=x[0]
    a=[0,0]

    # for i in range(1,len(x)):
    #     runsum+=x[i]
    #     if runsum>best:



def solution(nums):
    maxsofar = nums[0]
    maxendinghere=nums[0]

    for i in range(1,len(nums)):
        maxendinghere=max(maxendinghere + nums[i], nums[i])
        maxsofar=max(maxsofar,maxendinghere)
    return maxsofar


def findmaxsubarray(arr,k):
    maxValue=float('-inf')
    runningsum=arr[0]

    for i in range(len(arr)):
        runningsum+=arr[i]
        if i>=k-1:
            maxValue=max(maxValue,runningsum)
            runningsum-=arr[i-(k-1)]

    return maxValue


a=[-2,1,-3,4,-1,2,1,-5,4]
print(findmaxsubarray(a,3))
