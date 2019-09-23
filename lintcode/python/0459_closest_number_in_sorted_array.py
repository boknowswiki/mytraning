#!/usr/bin/python -t

# binary search solution, time O(logn) space O(1)

class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return -1
        l = 0
        r = n - 1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        if abs(A[l-1]-target) < abs(A[l]-target):
            return l-1
        else:
            return l

