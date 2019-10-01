#!/usr/bin/python -t

# binary search, similar to 0183 wood cut

class Solution:
    """
    @param A: an array
    @param n: an integer
    @return: makes the smallest absolute value of the difference between any two elements to largest
    """
    def maximumAbsolutValue(self, A, n):
        # Write your code here
        if not A:
            return 0
        
        A.sort()
        
        l = 0
        r = A[-1]-A[0]
        
        while l < r:
            mid = l + (r-l)/2
            if self.getNum(A, mid) >= n:
                l = mid+1
            else:
                r = mid
                
        if self.getNum(A, l) >= n:
            return l
        else:
            return l-1
                
            
            
    def getNum(self, A, gap):
        cnt = 1
        lastNum = A[0]
        
        for i in range(1, len(A)):
            if A[i] - lastNum >= gap:
                lastNum = A[i]
                cnt += 1
                
        return cnt

