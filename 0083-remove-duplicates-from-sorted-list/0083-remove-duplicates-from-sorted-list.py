# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
            
        currNode, helperNode = head, head.next

        while helperNode:
            if currNode.val == helperNode.val:
                helperNode = helperNode.next
            else:
                currNode.next = helperNode
                currNode = helperNode
                helperNode = helperNode.next
        
        currNode.next = helperNode

        return head