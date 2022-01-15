#!/usr/bin/python -t

# binary search


import sys, math

class Solution:
    """
    @param piles: an array
    @param H: an integer
    @return: the minimum integer K
    """
    def minEatingSpeed(self, piles, H):
        # Write your code here
        m = len(piles)
        start = 1
        end = max(piles)
        #print(start, end)

        while start + 1 < end:
            mid = (start+end)//2
            hour = self.getHour(piles, mid)
            if hour <= H:
                end = mid
            else:
                start = mid

        if self.getHour(piles, start) <= H:
            return start

        return end

    def getHour(self, piles, val):
        hour = 0
        for i in range(len(piles)):
            hour += math.ceil(piles[i]/val)

        return hour


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

