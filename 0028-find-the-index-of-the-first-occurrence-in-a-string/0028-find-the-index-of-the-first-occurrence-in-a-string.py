class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

        return haystack.find(needle)

        '''
        if haystack == needle:
            return 0

        L, R, M = 0, 0, 0

        while R < len(haystack):
            if M == len(needle):
                return L
            if haystack[R] == needle[M]:
                R += 1
                M += 1
            else:
                R += 1
                L = R
                M = 0
        
        return R-1 if M == len(needle) else -1
        '''