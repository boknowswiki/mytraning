#!/usr/bin/python3 -t

# binary search
# time O(logn)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        n = len(a)
        if n == 0:
            return 0

        start = 0
        end = n-1

        while start + 1 < end:
            mid = start + (end-start)//2
            if a[mid] > a[mid+1]:
                end = mid
            else:
                start = mid

        return start if a[start] > a[end] else end


if __name__ == '__main__':
    s = Solution()
    a = [1,2,4,8,6,3]

    print(s.find_peak(a))

# binary search solution
# better and cleaner

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        n = len(A)
        l = 0
        r = n-1
        
        while l+1 < r:
            mid = (r+l)/2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid+1]:
                r = mid
            else:
                l = mid
                
        if A[l] > A[r]:
            return l
        else:
            return r


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        n = len(A)
        
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid+1]:
                l = mid +1
            else:
                r = mid
                
        return l

if __name__ == '__main__':
    s = [1,2,1,3,4,5,7,6]
    ss = Solution()
    print "answer is\n"
    print ss.findPeak(s)
