class Solution:
    def pivotInteger(self, n: int) -> int:
        
        helper = [1] 

        for i in range(1, n+1):
            
            b = sum(range(i, n+1))
            print(helper, b)
            if helper[0] == b:
                return i
            
            helper[0] += i+1

        return -1