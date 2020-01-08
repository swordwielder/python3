arr=[2,1,6,4,3,7]
def solution(arr):

    copy=arr
    # copy=[2,1,6,4,3,7]
    slices=[]
    # min_idx=2
    while len(copy) > 0:
        min_idx=copy.index(min(copy))
        slices.append(copy[:min_idx+1])
        print(slices) #[2,1]
        copy=copy[min_idx+1:]  # copy = [6,4,3,7]
    return len(slices)
print(solution(arr))
