# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1. Since we do not know the parent Node, we just use the given node to:
        # 1.1 Change its value to the following node
        # 1.2 Change its next to the .next.next of the following node
        node.val = node.next.val
        node.next = node.next.next