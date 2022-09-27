#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l + 1 < r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
                
        return r

#time O(logn) space O(1)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while l < r:
            m = l + (r-l)/2
            
            bad = isBadVersion(m)
            
            if bad:
                r = m 
            else:
                l = m+1

        return l
