# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        # METHOD 2: DOUBLING
        # Consists in doing: PREVIOUS BINARY VAL (0/1) * 2 + CURR BINARY VAL (0/1)
        
        # 1. Assign the 'previous' binary value to ans
        ans = head.val
        # 2. Move the head by one, simulating the 'CURR' value
        head = head.next

        # 3. If we still have values, we move through the LL
        while head:
            # Do the formula BEFORE * 2 + CURR, move the head
            ans = (ans * 2) + head.val
            head = head.next

        # 4. Return the sum
        return (ans)

        '''
        METHOD 1: Find lenght of LL

        1. Initialize a counter and a dummy head
        counter = -1
        prev = head

        2. Traverse the LL and find the lenght
        while head:
            counter += 1
            head = head.next
        
        3. Return the head to it's original state and traverse again, using pow by 2 in the corresponding index
        head = prev
        while head:
            print(head.val)
            if head.val != 0:
                ans += pow(2, counter)
            counter -= 1
            head = head.next
        
        4. Return the sum
        return ans
        '''