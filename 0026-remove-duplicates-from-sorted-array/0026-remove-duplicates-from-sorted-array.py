class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = 1

        while R < len(nums):
            # 1. Check if index L == R
            if nums[L] == nums[R]:
                # 2. If yes, we need to change R until we find a different value
                R+=1
            # 3. Else, it means we found a unique value, and it should change (NOTE: R doesnt change because each value appears only once)
            else:
                # Change value next to idx L
                nums[L+1] = nums[R]
                # Change idx L
                L+=1

        # Simply return where L is and add 1
        return L+1
        
        print(nums)