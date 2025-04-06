class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        seen = set()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            L, R = i + 1, n - 1
            while L < R:
                t = (nums[i], nums[L], nums[R])
                total = sum(t)
                if total == 0:
                    seen.add(t)
                    L += 1
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    R -= 1

        return list(seen)
            
