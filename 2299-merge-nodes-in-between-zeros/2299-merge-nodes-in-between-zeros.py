# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Initialize variables (first is 0, so we skip that one)
        head = head.next
        # 2. Create two helper pointers to keep track of new head + sum variable
        temp = currNode = None
        acum = 0

        # 3. While we have values
        while head:
            acum = 0
            # 4. Start adding until we get to a 0
            while head.val != 0:
                acum += head.val
                head = head.next
            # 5. If we have a CurrNode, then chain it to the LL
            if currNode:
                currNode.next = ListNode(acum)
                currNode = currNode.next
            # 6. This will only run once, the first time (add the first node and keep track of it)
            else: 
                currNode = ListNode(acum)
                temp = currNode

            # 7. Update head
            head = head.next

        # Return the new head
        return temp
        

            