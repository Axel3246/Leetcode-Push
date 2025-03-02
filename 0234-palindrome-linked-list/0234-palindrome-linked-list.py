# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        ans_arr = []
        
        # Traverse the Linked List and append to array
        while head:
            ans_arr.append(head.val)
            head = head.next
        
        # Generate Pointers
        L, R = 0, len(ans_arr)-1

        # Check if the content is ==
        while L < R:
            if ans_arr[L] != ans_arr[R]:
                return False
            L += 1
            R -= 1

        return True

        #return ans_arr == ans_arr[::-1]


