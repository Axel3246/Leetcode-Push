# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # 1. Create 3 pointers: NEW LIST - CURR of HEAD - HELPER HEAD
        newLL = currNode = helper = None

        # 2. While we still have elements in OG list
        while head:
            # 3. We check if head.value is not val
            if head.val != val:
                if newLL: # If we already have elements on new LL, create a new node for them
                    newLL.next = ListNode(head.val)
                    newLL = newLL.next
                else: # If its our first element, initialize the LL
                    newLL = ListNode(head.val)
                    helper = newLL
            # Update the head
            head = head.next
                
        return helper






