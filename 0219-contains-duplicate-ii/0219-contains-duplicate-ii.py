class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        hmap = {}

        for i in range(0, len(nums)):
            val = nums[i]
            if val in hmap:
                new = abs(hmap.get(val)-i)
                if new <= k:
                    return True
                else:
                    hmap[val] = i
            else:
                hmap[val] = i
        print(hmap)
        return False