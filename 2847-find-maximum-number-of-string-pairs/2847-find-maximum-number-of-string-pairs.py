class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        hmap = {}
        count = 0
        for word in words:
            if word[::-1] in hmap:
                count += 1
            else:
                hmap[word] = hmap.get(word, 0) + 1
        
        return count