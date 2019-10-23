#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        deps = {i:[] for i in range(numCourses)}
        level = [0 for i in range(numCourses)]
        
        for i, j in prerequisites:
            deps[j].append(i)
            level[i] += 1
            
        q, cnt = deque(), 0
        
        for i in range(numCourses):
            if level[i] == 0:
                q.append(i)
                
        while len(q) > 0:
            c = q.popleft()
            cnt += 1
            
            for d in deps[c]:
                level[d] -= 1
                if level[d] == 0:
                    q.append(d)
                    
        return cnt == numCourses
        

