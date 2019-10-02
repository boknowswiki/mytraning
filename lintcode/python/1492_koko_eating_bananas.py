#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param piles: an array
    @param H: an integer
    @return: the minimum integer K
    """
    def minEatingSpeed(self, piles, H):
        # Write your code here
        n = len(piles)
        r = max(piles)
        l = 1
        
        while l < r:
            mid = l + (r-l)/2
            total = 0
            for p in piles:
                total += (p+mid-1)/mid
            if total > H:
                l = mid+1
            else:
                r = mid
                
        return l

