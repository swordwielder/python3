import time

def reorder(arr):         
    sortedarr = sorted(arr)
    newarr = []
    
    end = len(sortedarr)-1
    for i in range(len(sortedarr)):
        newarr.append(sortedarr[end])
        newarr.append(sortedarr[i])
        end-=1
        
        if i >= end:
            break
    
    return newarr

# 
# Your previous Plain Text content is preserved below:
# lol it didn't run
# /**
# Given an unsorted array nums, reorder it such that nums[0] >= nums[1] <= nums[2] >= nums[3]....
# 
# Examples:
#   
#  Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
#  Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
#                  {20, 5, 10, 2, 80, 6, 100, 3}
# 
#  Input:  arr[] = {20, 10, 8, 6, 4, 2}
#  Output: arr[] = {20, 8, 10, 4, 6, 2} OR
#                  {10, 8, 20, 2, 6, 4}
# 
#  Input:  arr[] = {2, 4, 6, 8, 10, 20}
#  Output: arr[] = {4, 2, 8, 6, 20, 10}
# 
#  Input:  arr[] = {3, 6, 5, 10, 7, 20}
#  Output: arr[] = {6, 3, 10, 5, 20, 7}
#  Have you used jupyter notebook? YES its great
# **/
# 
# 
# How many interviews you had with FUBO? 


             
        
        
        
        
        
        
        
        
        
    
        
        
        
        
def order0(arr):
    for i in range(1,len(arr)):
        
        if i % 2 == 0:
            if arr[i-1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
        else:
            if arr[i-1] < arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
    return arr 

      
def order1(arr):
    arr.sort()
    for i in range(0,len(arr), 2): 
        arr[i], arr[i+1] = arr[i+1], arr[i] 
    
    return arr


def order2(arr):
    
    for i in range(0, len(arr), 2): 
        if (i> 0 and arr[i] < arr[i-1]): 
            arr[i],arr[i-1] = arr[i-1],arr[i] 
          
        if (i < len(arr) and arr[i] < arr[i+1]): 
            arr[i],arr[i+1] = arr[i+1],arr[i] 
            
    return arr

                   
inputarr= [20, 10, 8, 6, 4, 2]
start = time.time()
print(f'yours: {reorder(inputarr)}')
end= time.time()
print(end-start)
start= time.time()
print(f'O(n): {order0(inputarr)}' )
end= time.time()
print(end-start)
