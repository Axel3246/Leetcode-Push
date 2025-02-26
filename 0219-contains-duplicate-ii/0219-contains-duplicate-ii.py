class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        swind = set()
        L, R = 0, 1

        # Iterate through the arr
        for R in range(len(nums)):
            
            # If R - L > k, we got an invalid window, so we need to 'update' L until its valid again
            if R - L > k:
                swind.remove(nums[L])
                L += 1
            
            # If nums[R] is in window, return True
            if nums[R] in swind:
                return True
            swind.add(nums[R])
        
        return False