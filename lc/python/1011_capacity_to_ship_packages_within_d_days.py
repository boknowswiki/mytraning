#!/usr/bin/python -t

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l, r = max(weights), sum(weights)
        
        while l < r:
            mid, need, cur = l + (r-l)/2, 1, 0
            
            for w in weights:
                if cur + w > mid:
                    need = need + 1
                    cur = 0
                cur = cur + w
                
            if need > D:
                l = mid + 1
            else:
                r = mid
        
        return l
