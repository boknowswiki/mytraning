#!/usr/bin/python -t

# linked list


class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    
    def __init__(self):
        self.head = self.tail = None
        
        
    def enqueue(self, item):
        # write your code here
        if self.head == None:
            self.head = self.tail = Node(item)
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
            

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.head == None:
            return None
        else:
            val = self.head.val
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                
        return val
        
