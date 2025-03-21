class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        for idx, num in enumerate(nums):
            if num % 2 == 0:
                nums[idx] = 0
            else:
                nums[idx] = 1
        
        nums.sort()
        return nums
        