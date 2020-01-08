class Solution:
    def twoSum(self, nums, target):
        b=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if target==nums[i]+nums[j] and i!=j:
                    b.append(i)
                    b.append(j)
                    return b
        return None


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            print(i)
            if n not in h:
                h[num] = i
            else:
                #print(i)
                return [h[n], i]

nums = [2, 7, 11, 15]
target = 9
a=Solution2()
print(a.twoSum(nums,target))
