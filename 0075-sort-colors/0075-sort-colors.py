class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort - Modified
        # 1. Search for maximum in nums and sum + 1
        maxNum = max(nums) + 1
        L, R = 0, 0

        # 2. Create a count array of lenght maxNum + 1 (to store the occurences)
        countArr = [0] * maxNum

        # 3. Start counting the occurence of each value in the input array. Add this occurences in the 
        # corresponding index of the count array (where countArr[idx] = num)
        for num in nums:
            countArr[num] += 1

        # 4. Do the cumulative sum for each index of the countArr (this step does not help for this problem)
        '''
        for i in range(1, len(countArr)):
            countArr[i] = countArr[i] + countArr[i-1]
        '''

        # 5. With the original count, traverse the count array and append the 'indexes' where the value is not 0
        while L < len(nums):
            if countArr[R] != 0:
                nums[L] = R
                L += 1
                countArr[R] -= 1
            else:
                R += 1
            #print(nums)
        
        print(nums)


        



        