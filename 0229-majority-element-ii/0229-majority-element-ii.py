class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # 1. Create a hash map to func as a COUNTER and a list for the nums
        hmap = {}
        ans = []
        n = len(nums)

        # 2. Count the appearances of each num
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        # 3. See which keys satisfy the condition of KEY VALUE > N // 3
        for key, val in hmap.items():
            if val > n // 3:
                ans.append(key)
        
        return ans