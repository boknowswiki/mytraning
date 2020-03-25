#!/usr/bin/python -t

# array, sort
# time O(log(m+n))


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n//2+1)
        else:
            small = self.findKth(A, 0, B, 0, n//2)
            large = self.findKth(A, 0, B, 0, n//2+1)
            
            return (small+large)/2.0
            
    def findKth(self, A, startA, B, startB, k):
        if startA == len(A):
            return B[startB+k-1]
        if startB == len(B):
            return A[startA+k-1]
        if k == 1:
            return min(A[startA], B[startB])
            
        valA = A[startA+k/2-1] if startA+k/2 <= len(A) else sys.maxint
        valB = B[startB+k/2-1] if startB+k/2 <= len(B) else sys.maxint
        
        if valA < valB:
            return self.findKth(A, startA+k/2, B, startB, k-k/2)
        else:
            return self.findKth(A, startA, B, startB+k/2, k-k/2)
            
        
        
