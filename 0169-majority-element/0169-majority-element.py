class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}

        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        
        return max(hmap, key=hmap.get)