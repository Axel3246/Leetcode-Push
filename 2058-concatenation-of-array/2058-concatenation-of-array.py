class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0] *len(nums)*2
        n = len(nums)

        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i-n] = nums[i]
        
        return arr