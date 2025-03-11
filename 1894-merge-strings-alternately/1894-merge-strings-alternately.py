class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        li, ri = 0, 0
        lowest = min(len(word1), len(word2))
        ans = ''

        for i in range(lowest):
            ans += word1[li]
            ans += word2[ri] 
            li += 1
            ri += 1
        
        ans+=word1[li:]
        ans+=word2[ri:]

        return ans
