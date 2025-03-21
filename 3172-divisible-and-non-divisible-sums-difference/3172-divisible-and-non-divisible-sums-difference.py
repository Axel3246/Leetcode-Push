class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        ans = [0, 0]

        for i in range(1, n+1):
            if i % m == 0:
                ans[0] += i
            else:
                ans[1] += i
        
        return ans[1] - ans[0]