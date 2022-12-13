# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            for i in range(m):
                cur = cur.next
                if cur == None:
                    break
            if cur == None:
                break
            tmp = cur.next
            if tmp == None:
                break
            for i in range(n):
                tmp = tmp.next
                if tmp == None:
                    break
            cur.next = tmp
            
        return dummy.next
