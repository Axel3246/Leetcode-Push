class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # Check if we have elements first, if not return empty
        if len(nums) == 0:
            return []

        # 1. Initialize L pointer, R pointer (sliding window)
        L, R = 0, 1
        
        # 2. Variables to keep the 'range' and to construct the string
        ranged = ''
        ans = []

        # 3. We iterate until R is greater than the lenght of nums
        while R != len(nums):

            # 4. CASE 1: We find out that theres a number follow up (i.e 0, 1, 2 ...)
            # In this case we just move R to the right
            if nums[R] == nums[R-1] + 1:
                R += 1
            else:
            # 5. CASE 2: We find out that we're not following a range anymore
                # 6. CASE 2.1: If L pointer is just one less than R, it means we don't have a range, so just append L
                if L == R-1:
                    ans.append(str(nums[L]))
                else:
                # 7. CASE 2.2: Else, we know that we have a range, so we append accordingly by constructing the string
                # Then we just move the window
                    ranged = str(nums[L]) + '->' + str(nums[R-1])
                    ans.append(ranged)
                L = R
                R += 1

        # 8. We need to repeat the else, because we need to append the last range or element, depending on the position
        # of the pointers
        if L == R-1:
            ans.append(str(nums[R-1]))
        else:
            ranged = str(nums[L]) + '->' + str(nums[R-1])
            ans.append(ranged)
        
        # 9. Return the answer
        return ans
            
            
