class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hmap = {}

        for char in magazine:
            hmap[char] = hmap.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in hmap:
                return False
            elif char in hmap and hmap[char] > 0:
                hmap[char] -= 1
            else:
                return False
        
        return True