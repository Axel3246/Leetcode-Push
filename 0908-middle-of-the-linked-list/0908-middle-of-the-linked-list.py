# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1. Create a slow and fast pointer (slow will be half of fast when fast reaches the end)
        slow, fast = head, head

        # 2. Important condition: We need to see if we can still access fast and fast.next, to avoid a None.next. 
        # Ejemplo con una lista de longitud impar
        # Lista: 1 → 2 → 3 → 4 → 5 → None

        # Iteración   slow   fast   fast.next
        # Inicial      1      1       2
        # 1ª           2      3       4
        # 2ª           3      5      None
        # Fin

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 3. Return slow, which contains the remainder of the LL
        return slow

        '''
        To array
        currNode = head
        count = 0
        ans = []
        while currNode:
            count += 1
            currNode = currNode.next

        count = floor(count/2)
        while head:
            if count > 0:
                count -= 1
            else:
                ans.append(head.val)
            head = head.next
        
        return ListNode(ans)
    '''

        
            