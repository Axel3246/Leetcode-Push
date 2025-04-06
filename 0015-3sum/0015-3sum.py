class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)-1
        nums.sort()
        #print(nums)

        seen = set()

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i+1, n

            while(L < R):
                t = (nums[i], nums[L], nums[R])
               # print(t)
                if sum(t) == 0 and t not in seen:
                    seen.add(t)
                    R -= 1
                elif sum(t) < 0:
                    L += 1
                else:
                    R -= 1


        return list(seen)
            
