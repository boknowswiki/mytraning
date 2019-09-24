#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return -1
        
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                return mid
                
            if A[mid] >= A[l]:
                if A[l] <= target < A[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                if A[mid] < target <= A[r]:
                    l = mid+1
                else:
                    r = mid
                    
        print l
        if A[l] == target:
            return l
        else:
            return -1

if __name__ == '__main__':
    s = [4,3]
    t = 3
    s = [1,2,3]
    t = 1
    ss = Solution()
    print "answer is\n"
    print ss.search(s, t)
