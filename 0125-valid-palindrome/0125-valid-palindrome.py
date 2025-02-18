class Solution:
    def isPalindrome(self, s: str) -> bool:

        # .isalnum() keeps the ASCII characters
        s = ''.join(char.lower() for char in s if char.isalnum())
        L = 0
        R = len(s)-1

        # Traverse the string with 2 pointers, if they differ, return False
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True
