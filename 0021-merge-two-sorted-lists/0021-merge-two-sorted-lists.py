# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create a two pointers - a dummy head and a node to iterate
        dummyNode = ListNode(0)
        currNode = dummyNode

        # 2. While we don't end up in a None in either list
        while list1 and list2:
            # 3. If the value of the first list is smaller or equal to the value of the second
            # set currNode.next to list1 and advance list1
            if list1.val <= list2.val:
                currNode.next = list1
                list1 = list1.next
            # 4. Else, we find out that the list2.val is smaller, so we set currNode.next to it
            # and advance list2
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next
        
        # 5. If we don't have the same length of lists, there will be missing nodes,
        # so we just check
        if list1:
            currNode.next = list1
        if list2:
            currNode.next = list2
        
        return dummyNode.next