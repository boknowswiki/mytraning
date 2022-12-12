# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        def get_len(node):
            if not node:
                return 0
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        len_a = get_len(headA)
        len_b = get_len(headB)

        while len_a > len_b:
            headA = headA.next
            len_a -= 1

        while len_b > len_a:
            headB = headB.next
            len_b -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
