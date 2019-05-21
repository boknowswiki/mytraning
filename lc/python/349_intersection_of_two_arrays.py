#!/usr/bin/python -t

#time O(m+n) space O(m+n)

class Solution(object):
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) > len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


#sort the two list, and use two pointer to search in the lists to find common elements.

class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    nums1.sort()
    nums2.sort()
    i = j = 0
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            if not (len(res) and nums1[i] == res[len(res)-1]):
                res.append(nums1[i])
            i += 1
            j += 1
    
    return res

#time O(nlogn) space O(1)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def bs(nums, i):
            n = len(nums)
            l = 0
            r = n - 1
            while l <= r:
                mid = l + (r-l)/2
                if nums[mid] == i:
                    return True
                elif nums[mid] < i:
                    l = mid+1
                else:
                    r = mid - 1
                    
            return False
        
        l2 = sorted(nums2)
        s = set()
        for i in nums1:
            if bs(l2, i):
                s.add(i)
                
        ret = list(s)
        
        return ret
