# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode(val=1)

        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        reversed_head = prev
        c = 1

        while prev:
            val = prev.val + c
            prev.val = val % 10
            c = val // 10
            if prev.next is None and c:
                prev.next = ListNode(val=c)
                break
            prev = prev.next

        prev = None
        head = reversed_head
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
