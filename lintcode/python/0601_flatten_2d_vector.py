#!/usr/bin/python -t

#

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.stack = []
        self.next_ele = None
        
        for ele in reversed(vec2d):
            self.stack.append(ele)
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.next_ele == None:
            self.hasNext()
            
        tmp, self.next_ele = self.next_ele, None
        
        return tmp
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.next_ele != None:
            return True
            
        while len(self.stack) != 0:
            ele = self.stack.pop()
            if type(ele) == int:
                self.next_ele = ele
                return True
            
            for elem in reversed(ele):
                self.stack.append(elem)
        return
        

