#!/usr/bin/python -t

# linked list

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        if not nums:
            return None
            
        dummy = ListNode(0)
        prev = dummy
        
        for num in nums:
            prev.next = ListNode(num)
            prev = prev.next
            
        return dummy.next
        
        
