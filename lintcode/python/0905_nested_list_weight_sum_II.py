#!/usr/bin/python -t

# bfs


from collections import deque

class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        # Write your code here.
        
        q = deque(nestedList)
        #q.append(nestedList)
        sum_list = []
        ret = 0
        
        while len(q) > 0:
            n = len(q)
            dep_sum = 0
            
            for _ in range(n):
                l = q.popleft()
                if l.isInteger():
                    dep_sum += l.getInteger()
                else:
                    l_list = l.getList()
                    
                    while l_list:
                        q.append(l_list.pop())
                        
            sum_list.append(dep_sum)
            
        total_dep = len(sum_list)
        
        for i in range(total_dep):
            ret += sum_list[i] * (total_dep-i)
            
        return ret
        
        

# dfs

class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        # Write your code here.
        self.depth = []
        
        self.dfs(nestedList, 0)
        
        ret = 0
        d = len(self.depth)
        for i in range(d):
            ret += (d-i) * (self.depth[i])
            
        return ret
        
    def dfs(self, nestedList, depth):
        if depth >= len(self.depth):
            self.depth.append(0)
            
        for i in nestedList:
            if i.isInteger():
                self.depth[depth] += i.getInteger()
            else:
                self.dfs(i.getList(), depth+1)
                
        return
    

