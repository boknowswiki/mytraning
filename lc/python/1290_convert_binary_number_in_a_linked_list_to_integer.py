# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        ret = 0

        while head:
            ret = ret * 2 + head.val
            head = head.next

        return ret
      
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        ret = []

        while head:
            ret.append(head.val)
            head = head.next

        val = 0
        for i in range(len(ret)):
            val = val*2 + ret[i]

        return val
