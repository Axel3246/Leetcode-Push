class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        L = 0
        R = 1

        while R < len(nums):
            if nums[L] == 0 and nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
            elif nums[L] != 0:
                L+=1
                R+=1
            else:
                R+=1