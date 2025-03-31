class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # 1. Do Operations
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # 2. If we dont have 0, then we just return the array
        if 0 not in nums:
            return nums

        # 3. Else, we find the first ocurrence of 0 and create an R pointer to swap
        L = nums.index(0)
        R = L + 1

        # 4. Rearrange Zeros
        while R < len(nums):
            if nums[L] == 0 and nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            else:
                R += 1
        
        return nums