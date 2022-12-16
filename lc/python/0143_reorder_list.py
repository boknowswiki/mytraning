# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        def reverse(node):
            if not node:
                return None

            prev = None

            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            return prev

        second_reversed = reverse(second)

        def merge(l1, l2):
            dummy = ListNode()
            prev = dummy
            index = 0

            while l1 and l2:
                if index % 2 == 0:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
                index += 1

            if l1:
                prev.next = l1
            if l2:
                prev.next = l2
            return dummy.next
                
        return merge(head, second_reversed)
