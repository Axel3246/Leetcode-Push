class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # 1. Create sum for left and right elements
        right = [0] * len(nums)
        left = [0] * len(nums)
        n = len(nums)

        # 2. Iterate through nums and create the PREFIX SUM of right and left elements
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i-1]
            right[i] = right[i-1] + nums[n-i]

        # 3. Reverse the right list 
        right.reverse()
        
        return [abs(left[i] - right[i]) for i in range(len(nums))]

       
        
        