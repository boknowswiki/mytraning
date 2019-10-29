#!/usr/bin/python -t

# BFS with heap


import heapq
from collections import deque

class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating 
    @return: the top k largest rating moive which contact with S
    """
    def topKMovie(self, rating, G, S, K):
        # Write your code here
        q = deque()
        h = []
        v = set()
        ret = []
        
        q.append(S)
        v.add(S)
        
        while len(q) > 0:
            cur = q.popleft()
            
            for r in G[cur]:
                if r in v:
                    continue
                if len(h) < K:
                    heapq.heappush(h, [rating[r], r])
                else:
                    if rating[r] > h[0][0]:
                        heapq.heappop(h)
                        heapq.heappush(h, [rating[r], r])
                       
                v.add(r)
                q.append(r)
        
        #print h        
        for ele in h:
            ret.append(ele[1])
         
        #print ret   
        return ret
        

