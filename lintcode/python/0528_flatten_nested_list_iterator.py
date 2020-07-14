#!/usr/bin/python -t

# recursive

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.next_ele = None
        self.stack = []
        
        for ele in reversed(nestedList):
            self.stack.append(ele)
            
        return
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.next_ele == None:
            self.hasNext()
        
        tmp, self.next_ele = self.next_ele, None
        return tmp
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        #print "hasnext", self.index, self.nl, self.l
        if self.next_ele:
            return True
            
        while len(self.stack):
            ele = self.stack.pop()
            if ele.isInteger():
                self.next_ele = ele.getInteger()
                return True
            for elem in reversed(ele.getList()):
                self.stack.append(elem)
                
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
