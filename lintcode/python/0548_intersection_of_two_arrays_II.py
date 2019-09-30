#!/usr/bin/python -t

# use hashmap

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        counts = collections.Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

# sort and two pointer

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        
        l1, l2 = 0, 0
        ret = []
        
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                l1 += 1
            elif nums1[l1] > nums2[l2]:
                l2 += 1
            else:
                ret.append(nums1[l1])
                l1 += 1
                l2 += 1
                
        return ret

