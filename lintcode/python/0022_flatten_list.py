#!/usr/bin/python -t

# recursive
# dfs

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        n = len(nestedList)
        if n == 0:
            return []
            
        ret = []
        
        self.dfs(nestedList, ret)
        
        return ret
        
    def dfs(self, l, ret):
        for ll in l:
            if type(ll) == int:
                ret.append(ll)
            elif type(ll) == list:
                self.dfs(ll, ret)
                
        return
    


# non-recursive


class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = [nestedList]
        flatten_list = []
        
        while stack:
            #print "start", stack
            top = stack.pop()
            #print "top", top
            if isinstance(top, list):
                for elem in reversed(top):
                    stack.append(elem)
                    #print "append", stack
            else:
                flatten_list.append(top)
                
        return flatten_list
