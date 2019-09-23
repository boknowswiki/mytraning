#!/usr/bin/python -t

# sort and binary search solution

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        m = len(nums1)
        n = len(nums2)
        if m == 0 or n == 0:
            return []
        nums1.sort()
        nums2.sort()
        
        ret = set()
        
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            
        for i in range(n):
            if self.found(nums1, nums2[i]):
                ret.add(nums2[i])
                
        return list(ret)
        
    def found(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)/2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid
                
        if nums[l] == target:
            return True
        return False

