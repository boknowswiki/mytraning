#!/usr/bin/python -t

# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None

            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt

            return prev

        l1_rev = reverse(l1)
        l2_rev = reverse(l2)

        dummy = ListNode()
        prev = dummy
        c = 0

        while l1_rev or l2_rev:
            a = l1_rev.val if l1_rev else 0
            b = l2_rev.val if l2_rev else 0

            val = (a+b+c) % 10
            c = (a+b+c) // 10
            prev.next = ListNode(val=val)
            prev = prev.next
            if l1_rev:
                l1_rev = l1_rev.next
            if l2_rev:
                l2_rev = l2_rev.next

        if c:
            prev.next = ListNode(val=c)
            prev = prev.next


        return reverse(dummy.next)

# stack

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        total_sum = 0
        carry = 0
        ans = ListNode()
        while s1 or s2:
            if s1:
                total_sum += s1.pop()
            if s2:
                total_sum += s2.pop()

            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans

        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def dump_list(l):
    while l:
        print l.val
        l = l.next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_list = ListNode(0)
        prev_node = ret_list
        def reverse_l(l):
            if l == None:
                return None
            dummy = ListNode(0)
            prev = dummy
            head = l
            while head:
                temp = head.next
                head.next = prev.next
                prev.next = head
                head = temp
                
            return dummy.next
        
        #dump_list(l1)
        #dump_list(l2)

        l1_rev = reverse_l(l1)
        l2_rev = reverse_l(l2)

        #dump_list(l1_rev)
        #dump_list(l2_rev)
        
        c = 0
        
        while l1_rev and l2_rev:
            val = (l1_rev.val + l2_rev.val + c)%10
            c = (l1_rev.val + l2_rev.val + c)/10
            
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = prev_node.next

            l1_rev = l1_rev.next
            l2_rev = l2_rev.next
            
        while l1_rev:
            val = (l1_rev.val + c)%10
            c = (l1_rev.val+c)/10
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = prev_node.next
            l1_rev = l1_rev.next
            
        while l2_rev:
            val = (l2_rev.val + c)%10
            c = (l2_rev.val+c)/10
            new_node = ListNode(val)
            prev_node.next = new_node
            prev_node = prev_node.next
            l2_rev = l2_rev.next
            
        if c:
            new_node = ListNode(c)
            prev_node.next = new_node
            
            
        prev_node = reverse_l(ret_list.next)

        dump_list(prev_node)
        return prev_node

if __name__ =='__main__':
    s = Solution()
    l1 = [7,2,4,3]
    l2 = [5,6,4]

    print l1, l2
    def convert_list(l):
        dummy = ListNode(0)
        prev = dummy
        for i in range(len(l)):
            new_node = ListNode(l[i])
            prev.next = new_node
            prev = prev.next
        return dummy.next

    list_1 = convert_list(l1)
    list_2 = convert_list(l2)

    #dump_list(list_1)
    #dump_list(list_2)
    
    print('%s\n' % (s.addTwoNumbers(list_1, list_2)))

