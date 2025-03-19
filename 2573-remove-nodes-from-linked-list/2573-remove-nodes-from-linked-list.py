# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = [head.val]
        head = head.next
        

        while head:
            if head.val > stack[-1]:
                while stack and stack[-1] < head.val:
                    stack.pop()
                stack.append(head.val)
            else:
                stack.append(head.val)

            head = head.next

        head = currNode = None
        for node in stack:
            if not head:
                currNode = ListNode(node)
                head = currNode
            else:
                currNode.next = ListNode(node)
                currNode = currNode.next
        
        return head