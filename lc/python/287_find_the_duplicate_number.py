#!/usr/bin/python -t

# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        dup = -1
        
        while l <= r:
            mid = l + (r-l)//2
            cnt = 0
            
            cnt = sum(num <= mid for num in nums)
            if cnt > mid:
                dup = mid
                r = mid-1
            else:
                l = mid+1
                
        return dup

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return nums[i]
            
        return -1

#another way to use hashtable to check
