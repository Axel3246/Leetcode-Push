class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = 0
        R = len(s)-1
        arr = [a for a in s]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        print(arr)
        while L < R:
            if arr[L] not in vowels and arr[R] not in vowels:
                L+=1
                R-=1
            elif arr[R] not in vowels and arr[L] in vowels:
                R-=1
            elif arr[L] not in vowels and arr[R] in vowels:
                L+=1
            else:
                arr[L], arr[R] = arr[R],arr[L]
                L+=1
                R-=1
        
        return ''.join(arr)
