#!/usr/bin/python -t

# binary search
# time O(n)
# space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid
                    
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

#time O(logn) space O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[mid] >= target and target >= nums[start]:
                    end = mid - 1
                else:
                    start = start + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

