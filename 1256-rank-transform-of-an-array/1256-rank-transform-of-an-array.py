class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        helper = arr[:]
        helper.sort()
        hmap = {}

        for num in helper:
            if num not in hmap:
                hmap[num] = len(hmap)+1
        
        for i in range(len(arr)):
            arr[i] = hmap[arr[i]]
        
        return arr