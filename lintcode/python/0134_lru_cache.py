#!/usr/bin/python -t


class Node:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.dummy = Node()
        self.tail = self.dummy
        self.cap = capacity
        self.key_to_prev = {}
        
    def add_to_tail(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
        
        return
        
    def move_to_tail(self, prev):
        node = prev.next
        
        if node == self.tail:
            return
        
        prev.next = node.next
        if node.next:
            self.key_to_prev[node.next.key] = prev
            node.next = None
            
        self.add_to_tail(node)
        
        return
    
    def remove_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
        return

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
            
        self.move_to_tail(self.key_to_prev[key])
        return self.key_to_prev[key].next.val
        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        print key, value
        if key in self.key_to_prev:
            self.move_to_tail(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
        else:
            self.add_to_tail(Node(key, value))
            if len(self.key_to_prev) > self.cap:
                self.remove_front()
                
        return

    def dump(self):
        cur = self.dummy

        print "dump list:\n"
        while cur.next:
            print cur.next.val
            cur = cur.next

        print "dump key to prev:\n"
        for k in self.key_to_prev:
            print k, self.key_to_prev[k].next.val

        return
        

if __name__ == '__main__':
    ss = LRUCache(2)
    print "answer is\n"
    print ss.set(2, 1)
    #print ss.dump()
    print ss.set(1, 1)
    print ss.get(2)
    print ss.set(4, 1)
    #print ss.dump()
    print ss.get(1)
    #print ss.get(2)
