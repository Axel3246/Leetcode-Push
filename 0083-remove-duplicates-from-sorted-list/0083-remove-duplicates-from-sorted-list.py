# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. If theres no head, then return head
        if not head:
            return head

        # 2. Create two nodes to relink nodes. Almost like a slow-fast approach
        currNode, helperNode = head, head.next

        # 3. While our fast node exists
        while helperNode:
            # 4. If we find that our val is not the same, we relink the nodes
            if currNode.val != helperNode.val:
                currNode.next = helperNode
                currNode = helperNode
            # 5. Else, we just advance the helper node
            helperNode = helperNode.next
        
        # 6. We link the last node possible node to helperNode, which should be None
        currNode.next = helperNode

        return head