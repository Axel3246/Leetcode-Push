class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # 1. Create a set of the numbers in the list
        ms = set(nums)
        # 2. Create a counter to count the longest sequence
        ans = 0

        # 3. Traverse through the created set
        for num in ms:
            # 4. If the current number doesn't have it's predecesor number, then we are at the start of a sequence
            if num - 1 not in ms:
                # 5. Maintain a counter that will grow by 1
                nxt = 1
                # 6. While we can sum 1 to num and that num is in the set
                while num + nxt in ms:
                    # 7. Grow nxt by 1
                    nxt += 1
                
                # 8. Update ans by getting the max value of ANS and NXT
                ans = max(ans, nxt)
        
        return ans
