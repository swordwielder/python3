class Solution(object):
    def removeElement(self, nums, val):
        for i in nums[:]:
            if i==val:
                nums.remove(i)
        return len(nums)
