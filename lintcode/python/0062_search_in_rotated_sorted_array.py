#!/usr/bin/python3 -t

# binary search
# time O(logn)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        # write your code here
        n = len(a)
        if n == 0:
            return -1
        if n == 1:
            return 0 if a[0] == target else -1

        start = 0
        end = n - 1
        while start + 1 < end:
            if a[start] == target:
                return start
            if a[end] == target:
                return end

            mid = start + (end-start)//2
            if a[mid] == target:
                return mid
<<<<<<< HEAD
            if a[start] <= a[mid]:
                if a[start] <= target <= a[mid]:
=======
            if a[start] < a[mid]:
                if a[start] < target < a[mid]:
>>>>>>> f51984138baf092e83cddd0cd500c3216643625b
                    end = mid
                else:
                    start = mid
            else:
<<<<<<< HEAD
                if a[mid] <= target <= a[end]:
=======
                if a[mid] < target < a[end]:
>>>>>>> f51984138baf092e83cddd0cd500c3216643625b
                    start = mid
                else:
                    end = mid

        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1



if __name__ == '__main__':
    s = Solution()
    a = [4, 5, 1, 2, 3]
    b = 1
    a = [0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    b = -9
    a = [1001, 10001, 10007, 1, 10, 101, 201]
    b= 10001

    print(s.search(a, b))

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
