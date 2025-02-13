class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create a Set so that we can only store the digit once
        myset = set()

        # Fill the set with the contents of nums
        for i in nums:
            myset.add(i)

        # Now, if the set is the same length as nums, it means there are no duplicates of a digit, hence returning False. On the other hand, if its not the same length, it means there is at least 1 digit that is duplicated, hence returning True.

        if(len(myset) == len(nums)):
            return False
        return True
        
        