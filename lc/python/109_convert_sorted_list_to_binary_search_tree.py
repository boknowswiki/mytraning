#!/usr/bin/python -t

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedlisttobst(self, start, end):
        if start > end:
            return None
        mid = (start + end) /2
        left = self.sortedlisttobst(start, mid-1)
        p = TreeNode(self.head.val)
        p.left = left
        self.head = self.head.next
        p.right = self.sortedlisttobst(mid+1, end)

        return p
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        

        self.head = head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n = n + 1

        return self.sortedlisttobst(0, n-1)

