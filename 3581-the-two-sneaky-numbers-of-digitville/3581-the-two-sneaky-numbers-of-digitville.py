class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        return [key for key,val in hmap.items() if val == 2]