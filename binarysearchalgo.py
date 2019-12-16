from random import randint
from timeit import timeit
from random import randint

arr =   [1, 7, 9, 12, 16, 17, 18, 19, 20, 22, 26, 27, 32, 33, 34, 36, 41, 43, 49, 50]
# #      Low                             Mid                                      Upper
# arr=[26, 27, 32, 33, 34, 36, 41, 43, 49, 50]
#     #L               MID                Upper
# arr=[26, 27, 32, 33]
# #    L   MID      U

# arr=[32, 33]
# #    L    U
# #    M  
# arr=[33]
# #    L   
# #    M
# #      


# is 33 in array

def findElement(n,arr):
    for i in arr:
        if n==i:
            return True
    return False

def binarySearch2(num2find, arr):
    low=0
    high=len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == num2find:
            return True
        else:
            if arr[mid] < num2find:
                low=mid+1
            else:
                u = mid+1
    return False

def binarySearch3(num2find, arr):
    low=0
    high=len(arr)-1
    a=arr
    while len(a)>1:
        mid=(high+low)//2
        a=arr[low:high]
        if arr[mid]>num2find:
            high=mid
        elif arr[mid]<num2find:
            low=mid
        else:
            return True
    return False

     

# print(findElement(13,arr))
print(binarySearch(7,arr))
# check to see 
