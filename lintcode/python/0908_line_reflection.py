#!/usr/bin/python -t

# hash table

# 计算对称轴 (max(x) + min(x)) / 2
# 用一个dictionary记录每个坐标有多少个点(如果点在对称轴上则不考虑)
# 遍历dictionary, check对于每一个坐标, 是否存在个数一样多的点在对称的坐标上
# 时空复杂度均为 O(n)


class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def isReflected(self, points):
        # Write your code here
        if not points:
            return True
            
        d = {}
        x_min = x_max = points[0][0]
        
        for p in points:
            d[(p[0], p[1])] = d.get((p[0], p[1]), 0) + 1
            x_min = min(x_min, p[0])
            x_max = max(x_max, p[0])
            
        #print x_max, x_min, d
        x_mid = float(x_max+x_min)/2
        
        for p in points:
            need_x = x_mid * 2 - p[0]
            if (need_x, p[1]) not in d or d[(p[0], p[1])] != d[(need_x, p[1])]:
                return False
                
        return True
        
