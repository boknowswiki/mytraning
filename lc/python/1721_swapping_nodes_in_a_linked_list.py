# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head

        for _ in range(1, k):
            cur = cur.next

        first = cur

        second = head

        while cur.next:
            second = second.next
            cur = cur.next


        second.val, first.val = first.val, second.val

        return head
