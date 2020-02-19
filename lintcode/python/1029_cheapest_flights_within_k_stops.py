#!/usr/bin/python -t

# BFS and heapq


import heapq

class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        if not flights:
            return -1
        
        graph = collections.defaultdict(list)
        for s, e, price in flights:
            graph[s].append((e, price))
            
        dist = {}
        seen = set()
        stk = [(0, src, -1)]
        
        while stk:
            price, city, stop = heapq.heappop(stk)
            
            if city == dst:
                return price
            
            if city in seen:
                continue
            
            if stop >= K:
                continue
                
            seen.add(city)
            dist[city] = price
            
            for nei, p in graph[city]:
                if nei in seen:
                    continue
                
                if nei in dist and dist[nei] < p + price:
                    continue
                
                dist[nei] = p + price
                heapq.heappush(stk, (p + price, nei, stop + 1))
                
        return -1
        
        


#该题目是一道加了限制的最短路题目, 即限制最多有 K + 1 条边构成.
#
#在Bellman-Ford或者Dijkstra最短路算法的基础上做一点修改即可.
#
#如果是Bellman-Ford(或者是由该算法优化而来的SPFA算法), 那么需要限制迭代次数, 最多 K + 1 条边, 只迭代 K + 1 次即可.
#
#同时还需要保证每一次迭代只会让边生长一次. (Bellman-Ford需要记录并判断, 而SPFA无需关注这一点)
#
#如果是Dijkstra算法, 则需要额外记录一下当前点距离源点的边数.
#
#该问题数据范围不大, 同时提供的是所有的边的集合, 所以很适合使用Bellman-Ford算法.


class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        distance = [sys.maxsize for i in range(n)]
        distance[src] = 0
        
        for i in range(0, K + 1):
            dN = list(distance)    	# 直接把最短路数组复制一遍, 用副本保存松弛的结果, 也可以保证每一轮迭代最多增加一条边, 不过执行效率略低
            for u,v,c in flights:
                dN[v]= min(dN[v], distance[u] + c)
            distance = dN
            
        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1
            
            
