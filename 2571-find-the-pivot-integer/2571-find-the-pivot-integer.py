class Solution:
    def pivotInteger(self, n: int) -> int:
        
        # 1. CREATE A HELPER VAR WHICH WILL HOLD THE SUM
        helper = 1 

        # 2. ITER THROUGH THE SERIES
        for i in range(1, n+1):
            
            # 3. GET THE VALUE FROM I THROUGH N (N+1 TO INCLUDE N)
            b = sum(range(i, n+1))

            # 4. CHECK IF BOTH SUMS MATCH, IF THEY DO RETURN THE PIVOT INT
            if helper == b:
                return i
            
            # 5. ELSE WE UPDATE OUR SUM
            helper += i+1
        
        return -1