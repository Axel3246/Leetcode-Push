class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Start two pointers
        L, R = 0,  0

        # Iterate until we reach the end of the shorter string (s)
        while L != len(s):

            # If we are at the end of the largest string, theres no subseq
            if R == len(t):
                return False
            
            # If we match, advance the two pointers
            if s[L] == t[R]:
                R += 1
                L += 1
            else: # Else just advance the one of the largest
                R += 1
        
        return True