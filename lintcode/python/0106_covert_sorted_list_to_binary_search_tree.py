#!/usr/bin/python -t

# linked list and dfs

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
            
        return self.dfs(head)
        
    def dfs(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
            
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        tmp = slow.next
        slow.next = None
        
        root = TreeNode(tmp.val)
        root.left = self.dfs(head)
        root.right = self.dfs(tmp.next)
        
        return root
        
        
