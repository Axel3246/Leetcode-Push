# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Case 1. No head we return None
        if head is None:
            return None

        # Case 2. We have something, so we create two helpers
        prev, post = None, None
        
        # 1. While we still have a head with a value
        while head.next:

            # 2. Assign prev node to head
            prev = head
            # 3. Move head 1 step
            head = head.next
            # 4. Assign the next direction of the previous node to the last memory address (post)
            prev.next = post
            # 5. Update the last memory address (node)
            post = prev

        # 6. Flip the next of the head to the previous node.
        head.next = prev
        return (head)

