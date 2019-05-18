#!/usr/bin/python -t

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        ret = []
        
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                i = i + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
            else:
                ret.append(nums1[i])
                i = i + 1
                j = j + 1
                
        return ret
