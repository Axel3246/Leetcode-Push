# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create two helper arrays, 1 pointer for the new LL and 1 pointer to keep the head
        a = []
        b = []
        head = currNode = None

        # 2. Traverse the first LL and save the values
        while l1:
            a.append(l1.val)
            l1 = l1.next 
        
        # 3. Traverse the second LL and save the values
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        # 4. Join the numbers by mapping them to a string and reversing them
        a = int(''.join(map(str, a[::-1])))
        b = int(''.join(map(str, b[::-1])))

        # 5. Generate the list of the sum of a+b
        c = list(map(int, str(a+b)))

        # 6. Create the new LL from C
        for num in c[::-1]:
            if currNode:
                currNode.next = ListNode(num)
                currNode = currNode.next
            else:
                currNode = ListNode(num)
                head = currNode

        # 7. Return the new LL
        return head
