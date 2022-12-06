# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_dummy = ListNode()
        even_dummy = ListNode()

        odd_prev, even_prev = odd_dummy, even_dummy
        index = 1
        while head:
            if index % 2 == 1:
                odd_prev.next = head
                odd_prev = odd_prev.next
            else:
                even_prev.next = head
                even_prev = even_prev.next
            head = head.next
            index += 1

        even_prev.next = None
        odd_prev.next = even_dummy.next

        return odd_dummy.next
