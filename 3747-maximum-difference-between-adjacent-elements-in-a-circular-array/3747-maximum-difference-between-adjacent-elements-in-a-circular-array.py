class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        msf = -1

        for i in range(0, len(nums)):
            print(nums[i], i)
            if i == len(nums)-1:
                adjR = abs(nums[i] - nums[0])
            else:
                adjR = abs(nums[i] - nums[i+1])
            
            adjL = abs(nums[i] - nums[i-1])
            print(adjL, adjR, msf)

            if adjL > msf and adjL >= adjR:
                msf = adjL
            elif adjR > msf and adjR >= adjL:
                msf = adjR
        
        return msf

