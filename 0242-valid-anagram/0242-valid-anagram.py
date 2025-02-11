class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # We use hmap to count the letters (in this case two)
        hmap1 = {}
        hmap2 = {}

        # Iterate through first string
        for c in s:
            hmap1[c] = hmap1.get(c, 0) + 1

        # Iterante through second string
        for c in t:
            hmap2[c] = hmap2.get(c, 0) + 1

        print(hmap1, hmap2)

        # Return the comparison of both hmap
        return hmap1 == hmap2