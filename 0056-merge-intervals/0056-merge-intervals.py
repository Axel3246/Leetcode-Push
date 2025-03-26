class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []
        L, R = 0, 1

        while R < len(intervals):
            if intervals[L][1] >= intervals[R][0]:
                intervals[L][1] = max(intervals[L][1], intervals[R][1])
                R += 1
            else:
                ans.append(intervals[L])
                L = R
                R += 1

        ans.append(intervals[L])
        
        return ans
