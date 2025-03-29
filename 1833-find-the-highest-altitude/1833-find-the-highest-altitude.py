class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # 0. If we only have one altitude, then we automatically return 0
        if len(gain) == 1 and gain[0] < 0:
            return 0
        elif len(gain) == 1 and gain[0] > 0:
            return gain[0]
        else:

            # 1. Generate ANSWER LIST
            ans = [0] * (len(gain) + 1)

            # 2. CALCULATE THE SUM STARTING FROM 0 AND LIST INDEX 1
            for i in range(1, len(gain)):
                ans[i] = ans[i-1] + gain[i-1]
                print(ans)
            
            # 3. CALCULATE THE LAST ALTITUDE NEEDED
            ans[i+1] = ans[i] + gain[i]

            
            return max(ans)