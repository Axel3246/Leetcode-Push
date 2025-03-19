# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Use a Monotonic Stack to keep track of the 'greater' values
        stack = [head.val]
        head = head.next

        # 2. Traverse the Linked List and check for the following
        while head:
            # 2.1 If we find a greater value, we need to modify our stack until the value either
            # the first value in the stack or it's not the greatest anymore
            if head.val > stack[-1]:
                while stack and stack[-1] < head.val:
                    stack.pop()
                stack.append(head.val)
            else: # 2.2 If we find something else, we just append
                stack.append(head.val)

            head = head.next

        # 3. Create a dummyHead and a new pointer to reconstruct the list from the stack
        dummy = ListNode(0)
        currNode = dummy

        # 4. Iterate through the stack and construct the new LL
        for node in stack:
            currNode.next = ListNode(node)
            currNode = currNode.next
        
        # 5. Simply return the node next to dummy
        return dummy.next
        return head