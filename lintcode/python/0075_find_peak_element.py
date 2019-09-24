#!/usr/bin/python -t

# binary search solution

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
