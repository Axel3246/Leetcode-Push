class Solution:
    def reverseWords(self, s: str) -> str:

        L = len(s)-1
        ans = ''
        while L > -1:
            
            if s[L] != ' ':
                R = L
                while s[L] != ' ' and L != -1:
                    print(s[L], L)
                    L -= 1
                ans = ans + s[L+1:R+1] + ' '
            else:
                L-=1
        
        return ans.rstrip()
            
