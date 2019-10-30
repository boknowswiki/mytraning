#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        if not graph:
            return False
        
        UNSEEN = 0
        WHITE = 1
        BLACK = -1
            
        n = len(graph)
        color = [0 for _ in range(n)]
        
        q = deque()
        
        for i in range(n):
            if color[i] != UNSEEN:
                continue
            
            q.append(i)
            color[i] = WHITE
            
            while len(q) > 0:
                node = q.popleft()
                for ele in graph[node]:
                    if color[ele] == UNSEEN:
                        color[ele] = -color[node]
                        q.append(ele)
                    elif color[ele] != -color[node]:
                        return False
                        
        return True
    
