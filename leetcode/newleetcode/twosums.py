class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if target==nums[i]+nums[j] and i!=j:
                    b.append(i)
                    b.append(j)
                    return b
        return None
