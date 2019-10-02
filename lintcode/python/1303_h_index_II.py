#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def hIndex(self, citations):
        # write your code here
        n = len(citations)
        l = 0
        r = n-1
        ret = 0
        
        while l < r:
            mid = l+(r-l)/2
            target = n-mid
            if citations[mid] < target:
                l = mid+1
                ret = max(ret, citations[mid])
            else:
                r = mid
                ret = max(ret, target)
                
        return ret

