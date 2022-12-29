#!/usr/bin/python -t

# two pointers
# time O(m+n)
# space O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        if not nums1:
            nums1 = nums2
            return

        index = m+n-1
        index1 = m-1
        index2 = n-1

        while index1 >= 0 and index2 >= 0:
            #print(f"index1 {index1}, index2 {index2}, index {index}")
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1

        while index2 >= 0:
            nums1[index] = nums2[index2]
            index -= 1
            index2 -= 1

        return

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

