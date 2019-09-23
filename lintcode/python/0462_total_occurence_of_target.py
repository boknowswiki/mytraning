#!/usr/bin/python -t

# binary search solution time O(logn) space O(1)

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] < target:
                l = mid + 1
            else:
                r = mid
        lower = l
        
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)/2
            if A[mid]<=target:
                l = mid+1
            else:
                r = mid
        upper = l
        
        if A[upper] == target:
            return upper-lower+1
        return upper - lower

