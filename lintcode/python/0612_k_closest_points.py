#!/usr/bin/python -t


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        hq = []
        for p in points:
            dist = self.get_dist(p, origin)
            heapq.heappush(hq, (-dist, -p.x, -p.y))
            if len(hq) > k:
                heapq.heappop(hq)

        ret = []
        while len(hq) > 0:
            dist, x, y = heapq.heappop(hq)
            ret.append(Point(-x, -y))

        #print(ret)
        ret.reverse()

        return ret

    def get_dist(self, p, o):
        return (p.x - o.x)**2 + (p.y-o.y)**2

# heap
# 基于 PriorityQueue 的方法
# PriorityQueue 里从远到近排序。当 PQ 里超过 k 个的时候，就 pop 掉一个。
# 时间复杂度 O(nlogk)O(nlogk)
# 
# 如果使用 Quick Select 离线算法：
# 0. 计算所有的点到原点的 distance -- O(n)
# 
# Quick Select 去找到 kth smallest distance -- O(n)
# 遍历所有 distance 找到 top k smallest distance -- O(n)
# 找到的 top k smallest points 按 distance 排序并返回 -- O(klogk)
# 总共 Quick Select 离线算法耗费时间 O(n + klogk)O(n+klogk)

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        ret = []
        
        for point in points:
            dist = self.getDist(point, origin)
            heapq.heappush(heap, (-dist, -point.x, -point.y))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        while len(heap) > 0:
            dist, x, y = heapq.heappop(heap)
            ret.append(Point(-x, -y))
            
        ret.reverse()
        
        return ret
            
