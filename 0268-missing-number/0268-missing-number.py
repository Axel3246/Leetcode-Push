class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        myset = set([i for i in range(len(nums)+1)])
        print(myset)
        for i in nums:
            if i not in myset:
                pass
            myset.remove(i)

        return (list(myset)[0])


        

        

