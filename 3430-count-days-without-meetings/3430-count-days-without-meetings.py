class Solution:
    def countDays(self, days: int, intervals: List[List[int]]) -> int:
        
        ms = set()
        intervals.sort()
        ans = []
        L, R = 0, 1

        # 2. We need to iterate through all intervals
        while R < len(intervals):
            # 3. If we find that the end of the first interval is greater than the start of the second interval
            if intervals[L][1] >= intervals[R][0]:
                # 4. We need to modify the first interval END to the max END DATE of the L or R interval
                intervals[L][1] = max(intervals[L][1], intervals[R][1])
                # 5. We move R pointer by one
                R += 1
            else:
                # 6. If we see that the condition is not met, we found and merged the interval, so append to ans, move L and add one to R
                ans.append(intervals[L])
                L = R
                R += 1
        
        ans.append(intervals[L])

        # 7. Now that we have the correct intervals, we just need to subtract the length of the range between start and date for each interval for the day
        for L, R in ans:
            days -= len(range(L, R+1))

        return days