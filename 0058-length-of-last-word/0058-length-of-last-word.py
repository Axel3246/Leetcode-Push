class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip(' ')

        n = len(s)-1
        cnt = 0

        while n > -1 and s[n] != ' ':
            cnt += 1
            n -= 1

        return(cnt)

        
