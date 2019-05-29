#!/usr/bin/python -t

length = len(citations)
        
        first = 0
        count = length
        
        while count > 0:
            step = count / 2
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                count -= (step + 1)
            else:
                count = step
        
        return length - first

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        l = 0
        r = n
        
        while l < r:
            m = l + (r-l)/2
            
            if citations[m] < n-m:
                l = m + 1
            else:
                r = m
                
        return n-l
