#!/usr/bin/python -t

# bfs and heap
# AC


import heapq, collections

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
        related_movies = self.bfs(G, S)
        #print related_movies
        
        heap = []
        ret = []
        
        for m in related_movies:
            if len(heap) >= K:
                heapq.heappushpop(heap, (rating[m], m))
            else:
                heapq.heappush(heap, (rating[m], m))
        
        #print heap
        
        ret = sorted([m for _, m in heap])
        
        return ret
        
        
    def bfs(self, g, s):
        q = collections.deque([s])
        v = set([s])
        ret = []
        
        while len(q) != 0:
            movie = q.popleft()
            ret.append(movie)
            for m in g[movie]:
                if m in v:
                    continue
                q.append(m)
                v.add(m)
                
        return ret[1:]
            

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
        

