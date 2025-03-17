# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 1. If no head, return false
        if head is None:
            return False
        
        # 2. Create two pointers, one fast and one slow
        slow, fast = head, head.next

        # 3. Superimportant condition for fast / slow problems:
        # Ejemplo con una lista de longitud impar
        # Lista: 1 → 2 → 3 → 4 → 5 → None

        # Iteración   slow   fast   fast.next
        # Inicial      1      1       2
        # 1ª           2      3       4
        # 2ª           3      5      None
        # Fin

        while fast and fast.next:
            # 4. If we manage to end in the same node we have a cycle, hence return True
            if slow == fast:
                return True

            # 5. Else, we just continue traversing
            slow = slow.next
            fast = fast.next.next 

        # 6. If we didn't find anything, return false
        return False