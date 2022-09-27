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
    
# hash map
# time O(m+n)
# space min(m, n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
    
        dic = {}
        ret = []
        
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
            
        for num in nums2:
            if num in dic:
                ret.append(num)
                dic[num] -= 1
                if dic[num] == 0:
                    del dic[num]
                    
        return ret
        

#binary search
#time max(O(mlogm), O(nlogn), O(mlogn) or max(O(mlogm), O(nlogn), O(nlogm)) space max(O(m), O(n))

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def lower_bound(nums, val):
            l = 0
            r = len(nums) - 1
            while l < r:
                m = l + (r-l)/2
                if nums[m] < val:
                    l = m+1
                else:
                    r = m
            return l
            
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        ret = []
        
        while i < len1:
            index = lower_bound(nums2, nums1[i])
            count1 = 0
            while index < len2 and nums2[index] == nums1[i]:
                count1 = count1 + 1
                index = index + 1
                
            count2 = 0
            while j < len1 and nums1[j] == nums1[i]:
                count2 = count2+1
                j = j + 1
            ret.extend([nums1[i]]*min(count1, count2))
            
            i = j
        return ret
