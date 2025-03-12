class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}

        # We traverse through idx and content
        for i,j in enumerate(nums):
            # We check if the residual of target = curr context is in our hashmap
            if(target - j) in hmap:
                return [i, hmap[target-j]] # if yes, we return the curr idx and the other idx
            hmap[j] = i # else, we just add the new element to the hashmap