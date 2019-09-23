#!/usr/bin/python -t

# binary search solution time O(logn) space O(1)

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
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
                
        if A[l] == target:
            return l
        if A[l] < target and l == n-1:
            return l+1
        return l

