# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_len(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next

            return cnt

        list_len = get_len(head)

        mod_val = list_len % k
        val = list_len // k
        ret = []
        cur = head

        for i in range(k):
            node = cur
            for j in range(val+(i<mod_val)-1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ret.append(node)
        return ret
