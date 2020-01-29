#!/usr/bin/python -t

# hash table
#两层for循环遍历每两个点，计算两点之间距离，以及可以构成该距离的的个数。
#用hash表记录Map<distance, count>
#则该距离下可构成回旋镖的个数为count * (count - 1)


class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """
    def numberOfBoomerangs(self, points):
        # Write your code here
        if not points or not points[0]:
            return 0
            
        ret = 0
        
        for i in range(len(points)):
            d_cnt = {}
            for j in range(len(points)):
                if i == j:
                    continue
                
                dis = self.getdis(points[i], points[j])
                cnt = d_cnt.get(dis, 0)
                d_cnt[dis] = cnt + 1
                
            for d in d_cnt:
                ret += d_cnt[d]*(d_cnt[d]-1)
                
        return ret
        
                
                
    def getdis(self, x, y):
        a = x[0] - y[0]
        b = x[1] - y[1]
        
        return a*a + b*b
        
        
