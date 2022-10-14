# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.get_len(head)
        if l == 1:
            return None
        mid = l//2
        cur = head
        
        while mid-1 > 0:
            cur = cur.next
            mid -= 1
            
        cur.next = cur.next.next
        
        return head
        
    def get_len(self, node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
            
        return cnt
