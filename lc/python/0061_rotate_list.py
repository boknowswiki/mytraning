# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        def get_len(node):
            cnt = 0
            tail = None
            while node:
                cnt += 1
                tail = node
                node = node.next
            return cnt, tail

        l, tail = get_len(head)

        k = k % l
        cur = head
        for _ in range(l-k):
            tail.next = cur
            cur = cur.next
            tail = tail.next
            tail.next = None

        return cur
