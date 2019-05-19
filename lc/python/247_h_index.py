#!/usr/bin/python -t

#time O(n) space O(n) with hash

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l = [0]*(n+1)
        
        for i in range(n):
            if citations[i] >= n:
                l[n] = l[n]+1
            else:
                l[citations[i]] = l[citations[i]] + 1
                
        paper = 0
        
        for i in range(n, -1, -1):
            paper = paper + l[i]
            if paper >= i:
                return i
            
        return 0


#time O(nlogn) space O(1) with sort

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        
        n = len(citations)
        
        for i in range(n):
            if citations[i] >= n - i:
                return n-i
            
        return 0
