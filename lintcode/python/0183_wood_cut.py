#!/usr/bin/python -t

# binary search
#使用九章算法强化班中所讲的基于答案值域的二分法。
#木头长度的范围在 1 到 max(L)，在这个范围内二分出一个长度 length，然后看看以这个 wood length 为前提的基础上，能切割出多少木头，如果少于 k 根，说明要短一些才行，如果多余 k，说明可以继续边长一些。
#
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
            
        max_l = max(L)
        l = 1
        r = 0
        r = max(r, max_l)
        ret = 0
        
        while l < r:
            mid = l + (r-l)/2
            if self.count(L, mid) >= k:
                ret = mid
                l = mid+1
            else:
                r = mid-1
                
        return l if self.count(L, l) >= k else l-1
                
    def count(self, L, target):
        t = 0
        for l in L:
            t += l/target
            
        return t

