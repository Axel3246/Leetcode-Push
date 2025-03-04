class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hmap = {}

        # Count the letters in the string
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1

        # Traverse the hmap and return the instance of the key with val 1
        # using .index()
        for key, val in hmap.items():
            if val == 1:
                return s.index(key)
        
        # If not found, return -1
        return -1