#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return False
        
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                return True
                
            if A[mid] > A[l]:
                if A[l] <= target < A[mid]:
                    r = mid
                else:
                    l = mid+1
            elif A[mid] < A[l]:
                if A[mid] < target <= A[r]:
                    l = mid+1
                else:
                    r = mid
            else:
                l += 1
                    
        print l
        if A[l] == target:
            return True
        else:
            return False

if __name__ == '__main__':
    s = [9,5,6,7,8,9,9,9,9,9,9]
    t = 8
    ss = Solution()
    print "answer is\n"
    print ss.search(s, t)
