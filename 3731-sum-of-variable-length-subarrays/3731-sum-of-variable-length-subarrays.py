class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = [0] * n
        ans[0] = nums[0]

        for i in range(1, n):
            start = max(0, i - nums[i])
            ans[i] = sum(nums[start:i+1])

        return sum(ans)