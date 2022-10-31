#!/usr/bin/python -t

# linked list, divide and conquer and merge sort
# time O(nlogn)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.helper(lists, 0, len(lists)-1)
    
    def helper(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start+end)//2
        l1 = self.helper(lists, start, mid)
        l2 = self.helper(lists, mid+1, end)
        
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        dummy = ListNode()
        prev = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
            
            
        if not l1:
            prev.next = l2
        if not l2:
            prev.next = l1
            
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2lists(l1, l2):
            ret = ListNode(0)
            head = ret

            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next

                head = head.next

            if l1 == None:
                head.next = l2
            elif l2 == None:
                head.next = l1

            return ret.next

        n = len(lists)
        if n == 0:
            return None
        end = n - 1

        while end > 0:
            start = 0

            while start < end:
                lists[start] = merge2lists(lists[start], lists[end])
                start = start + 1
                end = end - 1

        return lists[0]

