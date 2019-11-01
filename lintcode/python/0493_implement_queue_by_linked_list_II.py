#!/usr/bin/python -t

# linked list


class Node:
    def __init__(self, val, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val = val


class Dequeue:
    
    def __init__(self):
        # do intialization if necessary
        self.head = self.tail = None

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):
        # write your code here
        if self.head == None:
            new_node= Node(item)
            self.head = self.tail = new_node
            #self.head.prev = self.head.next = self.tail.prev = self.tail.next = new_node
        else:
            new_h = Node(item)
            new_h.next = self.head
            self.head.prev = new_h
            self.head = new_h

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):
        # write your code here
        if self.head == None:
            self.head = self.tail = Node(item)
        else:
            new_node = Node(item)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

    """
    @return: An integer
    """
    def pop_front(self):
        # write your code here
        if self.head == None:
            return None
        else:
            val = self.head.val
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                
        return val

    """
    @return: An integer
    """
    def pop_back(self):
        # write your code here
        if self.tail == None:
            return None
        else:
            val = self.tail.val
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = self.head = None
            
        return val
        

