#!/usr/bin/python -t

# binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n-1

        while l + 1 < r:
            mid = (l+r)//2
            if mid+1 < n and arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid

        if arr[r] > arr[l]:
            return r
        return l

#time O(lgn) space O(1)

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        l = 0
        r = n - 1
        
        while l < r:
            mid = l + (r-l)/2
            
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                l = mid+1
            else:
                r = mid-1
                
        return l

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        l = 0
        r = n - 1
        
        while l < r:
            mid = l + (r-l)/2
            
            if A[mid] < A[mid+1]:
                l = mid + 1
            else:
                r = mid
                
        return l
