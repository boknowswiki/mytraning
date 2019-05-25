#!/usr/bin/python -t

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
