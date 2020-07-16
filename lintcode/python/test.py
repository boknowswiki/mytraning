#!/usr/bin/python -t

class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.cap = capacity
        self.key_to_prev = {}
        self.head = Node(0, 0)
        self.tail = self.head
        

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        else:
            self.move_to_tail(self.key_to_prev[key])
            
        return self.key_to_prev[key].next.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.move_to_tail(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
        else:
            self.add_node(key, value)
            if len(self.key_to_prev) > self.cap:
                self.remove_head()
        return
    
    def move_to_tail(self, prev):
        node = prev.next
        
        if node != self.tail:
            self.key_to_prev[node.next.val] = prev
            prev.next = node.next
            node.next = None
        
            self.tail.next = node
            self.key_to_prev[node.val] = self.tail
            self.tail = node
        
        return
    
    def add_node(self, key, val):
        self.key_to_prev[key] = self.tail
        node = Node(key, val)
        self.tail.next = node
        self.tail = node
        
        return
    
    def remove_head(self):
        del self.key_to_prev[self.head.next.key]
        
        self.key_to_prev[self.head.next.next.key] = self.head
        self.head.next = self.head.next.next
        
        return


if __name__ == "__main__":
    l = LRUCache(2)
    l.set(2,1)
    l.set(1,1)
    print l.get(2)
    l.set(4,1)
    print l.get(1)
    print l.get(2)
