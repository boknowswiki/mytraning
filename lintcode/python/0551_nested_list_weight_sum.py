#!/usr/bin/python -t

# bfs

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

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0
            
        s = []
        ret = 0
        
        for n in nestedList:
            s.append((n, 1))
            
        while len(s) > 0:
            n, dep = s.pop()
            if n.isInteger():
                ret += n.getInteger()*dep
            else:
                l = n.getList()
                for ll in l:
                    s.append((ll, dep+1))
                    
        return ret
        
        

# dfs

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


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here

        return self.dfs(nestedList, 1)
        
    def dfs(self, nestedList, dep):
        if not nestedList:
            return 0
            
        ret = 0
        for i in nestedList:
            if i.isInteger():
                ret += i.getInteger() * dep
            else:
                ret += self.dfs(i.getList(), dep+1)
                
        return ret
        
       
