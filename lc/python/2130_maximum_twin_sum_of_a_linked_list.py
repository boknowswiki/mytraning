# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        def reverse(node):
            if not node:
                return node

            prev = None

            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            return prev

        l2 = reverse(second)

        ret = -sys.maxsize-1

        l1 = head
        
        while l1 and l2:
            ret = max(ret, l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next

        return ret
      
      
      
    def pairSum(self, head):
        slow, fast = head, head
        maximumSum = 0

        # Get middle of the linked list.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linked list.
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next
        
        start = head
        while prev:
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next
            start = start.next

        return maximumSum
