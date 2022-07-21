#!/usr/bin/python3 -t

# bfs
# time O(n)
# space O(n)


from typing import (
    List,
)

import collections

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        deps = {i:[] for i in range(num_courses)}
        cnt = [0 for i in range(num_courses)]

        for i, j in prerequisites:
            deps[j].append(i)
            cnt[i] += 1

        q = collections.deque([])
        num = 0

        for i in range(num_courses):
            if cnt[i] == 0:
                q.append(i)

        while len(q) > 0:
            cur = q.popleft()
            num += 1

            for d in deps[cur]:
                cnt[d] -= 1
                if cnt[d] == 0:
                    q.append(d)

        return num == num_courses


if __name__ == '__main__':
    s = Solution()
    a = 2
    b = [[1,0]]
    print(s.can_finish(a, b))

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
        

