#!/usr/bin/python -t

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
