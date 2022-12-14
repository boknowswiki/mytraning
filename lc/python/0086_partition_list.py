# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        less_head = ListNode()
        less_prev = less_head
        not_less_head = ListNode()
        not_less_prev = not_less_head

        while head:
            if head.val < x:
                less_prev.next = head
                less_prev = less_prev.next
            else:
                not_less_prev.next = head
                not_less_prev = not_less_prev.next

            head = head.next

        less_prev.next = not_less_head.next
        not_less_prev.next = None

        return less_head.next
