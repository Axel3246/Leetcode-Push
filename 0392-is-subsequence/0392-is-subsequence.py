class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        L, R = 0,  0

        while L != len(s):
            if R == len(t):
                return False
            
            if s[L] == t[R]:
                R += 1
                L += 1
            else:
                R += 1
        
        return True