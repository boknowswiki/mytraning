#!/usr/bin/python3 -t

# sort and two pointers
# time O(max(nlogn, mlogm))
# space O(1)

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
        if n == 0 or m == 0:
            return []

        nums1.sort()
        nums2.sort()

        ret = set()
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] == nums2[j]:
                ret.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j  += 1

        return list(ret)


if __name__ == '__main__':
    s = Solution()
    a = [1,2,2,1]
    b = [2,2]
    print(s.intersection(a, b))

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

