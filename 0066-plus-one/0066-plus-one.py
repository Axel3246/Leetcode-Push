class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        a = int(''.join(map(str,digits))) + 1
        b = list(map(int,str(a)))
        
        return b