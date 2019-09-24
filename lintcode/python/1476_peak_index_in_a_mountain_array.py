#!/usr/bin/python -t

class Solution:
    """
    @param A: an array
    @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    def peakIndexInMountainArray(self, A):
        # Write your code here
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] > A[mid - 1]:
                start = mid
            else:
                end = mid
        print start, end
        if A[start] > A[start + 1] and A[start] > A[start - 1]:
            return start
        else:
            return end

# binary search solution


class Solution:
    """
    @param A: an array
    @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    def peakIndexInMountainArray(self, A):
        # Write your code here
        n = len(A)
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            if A[mid-1] < A[mid] < A[mid+1]:
                l = mid+1
            if A[mid-1] > A[mid] > A[mid+1]:
                r = mid
                
        return l

if __name__ == '__main__':
    s = [0,1,0]
    ss = Solution()
    print "answer is\n"
    print ss.peakIndexInMountainArray(s)

