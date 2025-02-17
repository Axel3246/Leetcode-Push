class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1 = {}
        ans = ''

        for i, char in enumerate(s):
            if char not in h1:
                if t[i] in h1.values():
                    return False
                h1[char] = t[i]

        for j in s:
            ans += h1[j]

        
        return ans == t