class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Create a hashmap
        hmap = {}

        # Count the chars in the magazine
        for char in magazine:
            hmap[char] = hmap.get(char, 0) + 1
        
        # Check if we can construct the ransom letters with the counted ones
        for char in ransomNote:
            if char not in hmap:
                return False
            elif char in hmap and hmap[char] > 0:
                hmap[char] -= 1
            else:
                return False
        
        return True