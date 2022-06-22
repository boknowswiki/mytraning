#!/usr/bin/python3 -t

# binary search
# time O(logn)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        # write your code here
        ret = [-1, -1]
        if not a:
            return ret

        if len(a) == 1 and a[0] != target:
            return ret

        ret[0] = self.find_lower(a, target)
        ret[1] = self.find_higher(a, target)

        return ret

    def find_lower(self, a, target):
        start = 0
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end-start)//2
            if a[mid] >= target:
                end = mid
            else:
                start = mid

        if a[start] == target:
            return start
        if a[end] == target:
            return end

        return -1

    def find_higher(self, a, target):
        start = 0
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end-start)//2
            if a[mid] > target:
                end = mid
            else:
                start = mid

        if a[end] == target:
            return end
        if a[start] == target:
            return start

        return -1


if __name__ == '__main__':
    s = Solution()
    a = []
    a = [5, 7, 7, 8, 8, 10]
    b = 8
    print(s.search_range(a, b))

# binary search solution

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        n = len(A)
        
        l = self.lower_bound(A, target)
        r = self.upper_bound(A, target)
        
        return [l, r]
        
    def lower_bound(self, A, target):
        n = len(A)
        if n == 0:
            return -1
        l = 0
        r = n -1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        if A[l] == target:
            return l
        else:
            return -1
        
    def upper_bound(self, A, target):
        n = len(A)
        if n == 0:
            return -1
        l = 0
        r = n -1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] <= target:
                l = mid + 1
            else:
                r = mid
                
        if A[l] == target:
            return l
        elif A[l-1] == target:
            return l-1
        else:
            return -1

if __name__ == '__main__':
    s = [-1,0,1,2,2,2,3,3,3,4,4,4,5,5,6,90,92,93,101]
    t = 2
    ss = Solution()
    print "answer is\n"
    print ss.searchRange(s, t)
