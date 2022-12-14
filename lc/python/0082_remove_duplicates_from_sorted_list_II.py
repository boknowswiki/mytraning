# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next
