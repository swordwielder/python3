#Brute Force, inefficient method
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left=0
        right=0
        s=nums[0]
        a=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                a+=nums[j]
                if s<a:
                    s=a
            a=0
        return s

#leetcode solution
class Solution2:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

#Kadane's Algorithm?
class Solution3:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)
        return max_sum
