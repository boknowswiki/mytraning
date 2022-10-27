# linked list and divide and conquer
# time O(nlogn)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
    
    def helper(self, node):
        if not node:
            return None
        
        if not node.next:
            return node
        slow = node
        fast = node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = None
        
        l1 = self.helper(node)
        l2 = self.helper(second_half)
        
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
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
