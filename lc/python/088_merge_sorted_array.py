#!/usr/bin/python -t

#Time O(m+n), space O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        lt = m + n - 1
        
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[lt] = nums2[l2]
                l2 = l2 - 1
                
            else:
                nums1[lt] = nums1[l1]
                l1 = l1 -1
            lt = lt - 1
            
        while l2 >= 0:
            nums1[lt] = nums2[l2]
            lt = lt - 1
            l2 = l2 -1
            
        return

