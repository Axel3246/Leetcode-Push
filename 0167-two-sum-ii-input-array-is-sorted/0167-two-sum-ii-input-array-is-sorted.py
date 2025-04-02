class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 1. Create two pointers: One for the start, the other on the end
        L, R = 0, len(numbers)-1

        # 2. As there is one solution we dont care about the condition
        while L < R:
            currSum = numbers[R] + numbers[L]
            # 3. If we find the target return idx
            if currSum == target:
                return L+1, R+1
            # 4. If sum is larger than targer, we need to update R for it to be in a smaller number
            elif currSum > target:
                R -= 1
            # 5. If the sum is smaller than target, we need to update L for it to be in a greater number
            else:
                L += 1