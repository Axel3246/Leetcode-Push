class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []

        for i in nums1:
            stack = []
            idx2 = nums2.index(i)
            for j in range(idx2+1, len(nums2)):
                if nums2[j] > i and not stack:
                    stack.append(nums2[j])

            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])    
            

        return ans


            
