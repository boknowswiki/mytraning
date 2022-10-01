#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if mid >0 and mid < n-1 and nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if mid > 0 and nums[mid] > nums[mid-1]:
                l = mid
            else:
                r = mid
                
        if nums[l] > nums[r]:
            return l
        return r

if __name__ == "__main__":
    s = Solution()
    a = [1,2,3,1]
    a = [1,6,5,4,3,2,1]
    print(s.findPeakElement(a))

#time O(n) space O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
            
        return n-1

#time O(log2 ^ n) space O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        
        while start < end:
            mid = (start+end)/2
            
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid
                
        return start
