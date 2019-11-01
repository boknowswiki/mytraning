#!/usr/bin/python -t

# linked list and swap way

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        res = []
        while head:
            res.append(head.val)
            head = head.next
        for i in range(len(res) / 2):
            tmp = res[i]
            res[i] = res[len(res) - i - 1]
            res[len(res) - i - 1] = tmp
        return res

# linked list and dfs

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        if not head:
            return []
            
        ret = []
        self.helper(head, ret)
        
        return ret
        
    def helper(self, node, ret):
        if not node:
            return
        if node.next:
            self.helper(node.next, ret)
            
        ret.append(node.val)
        
        return
    
    
