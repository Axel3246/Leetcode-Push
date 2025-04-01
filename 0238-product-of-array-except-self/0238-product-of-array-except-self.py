class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1. Create ans array and a suffix product
        ans = [1] * len(nums)
        suffix = 1

        # 2. First Pass: Compute the prefix product of the idx
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        #print(f'First ITER {ans}')

        # 3. Using the SUFFIX PRODUCT VARIABLE, keep track of the product and multiply ans[IDX] by it
        for j in range(len(nums)-2, -1, -1):
            suffix *= nums[j+1]
            ans[j] = ans[j] * suffix
        
        #print(f'Second ITER {ans}')
        return ans
