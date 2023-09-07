# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        empty_node = None
        cur = end = prev.next
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = empty_node
            empty_node = cur
            cur = nxt

        prev.next = empty_node
        end.next = cur

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
