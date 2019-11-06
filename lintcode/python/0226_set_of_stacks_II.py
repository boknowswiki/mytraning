#!/usr/bin/python -t

# stack

class SetOfStacks2:
    """
    @param: capacity: an inetger, capacity of sub stack
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.s = []
        self.cap = capacity

    """
    @param: v: An integer
    @return: nothing
    """
    def push(self, v):
        # write your code here
        if len(self.s) == 0:
            self.s.append([])
        if len(self.s[-1]) == self.cap:
            self.s.append([])
            
        self.s[-1].append(v)
        
        return

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        v = self.s[-1].pop()
        if len(self.s[-1]) == 0:
            self.s.pop()
            
        return v

    """
    @param: index: The index of a specific sub-stack
    @return: top element of the specific sub-stack
    """
    def popAt(self, index):
        # write your code here
        return self.leftShift(index, True)
        
    def leftShift(self, index, remove_top):
        if remove_top:
            remove_item = self.s[index][-1]
            self.s[index].pop()
        else:
            remove_item = self.s[index][0]
            self.s[index].pop(0)
            
        if len(self.s[index]) == 0:
            self.s.pop(index)
        elif len(self.s) > index+1:
            v = self.leftShift(index+1, False)
            self.s[index].append(v)
            
        return remove_item
        
        
