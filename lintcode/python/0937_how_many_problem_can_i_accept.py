#!/usr/bin/python -t

# binary search

import math

class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """
    def canAccept(self, n, k):
        # Write your code here
        l = 0
        r = int(math.sqrt(2*n))
        #print r
        while l < r:
            mid = (l+r)/2
            val = k*(1+mid)*mid/2
            
            if val <= n:
                l = mid+1
            else:
                r = mid
                
            
        if k*(1+l)*l/2 > n:
            return l-1
        else:
            return l

