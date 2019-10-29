#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        deps = {i:[] for i in range(numCourses)}
        levels = [0 for i in range(numCourses)]
        
        for i, j in prerequisites:
            deps[j].append(i)
            levels[i] += 1
            
        q = deque()
        ret = []
        
        for i in range(numCourses):
            if levels[i] == 0:
                q.append(i)
                
        while len(q) > 0:
            c = q.popleft()
            ret.append(c)
            
            for dep in deps[c]:
                levels[dep] -= 1
                if levels[dep] == 0:
                    q.append(dep)
                    
        if len(ret) == numCourses:
            return ret
            
        return []
        

