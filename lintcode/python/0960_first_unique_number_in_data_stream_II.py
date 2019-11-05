#!/usr/bin/python -t

# linked list

class DataStream:
    
    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.dup = set()
        
    def push_back(self, n):
        self.tail.next = ListNode(n)
        self.num_to_prev[n] = self.tail
        self.tail = self.tail.next
        
        return
    
    def remove(self, n):
        prev = self.num_to_prev[n]
        prev.next = prev.next.next
        
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev
            
        return
        
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self.dup:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)
            return
        
        self.dup.add(num)
        self.remove(num)
        
        return

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        if not self.dummy.next:
            return None
        return self.dummy.next.val
        
        
            
