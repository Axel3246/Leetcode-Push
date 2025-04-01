class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        L, R = 0, 0
        ans = ''
        
        while R != len(word2) and L != len(word1):
            ans += word1[L]
            ans += word2[R]
            L += 1
            R += 1

        if R == len(word2):
            return ans + word1[L:]
        return ans + word2[R:]
