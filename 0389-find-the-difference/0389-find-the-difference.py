class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        hmap = {}

        # Count the letters in S
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        
        # Subtract the count by the letters that appear in T.
        # If the letter does not appear or it's count is 0
        # thats the extra letter
        for c in t:
            if c not in hmap or hmap[c] == 0:
                return c
            hmap[c] -= 1
        
