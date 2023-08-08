#!/usr/bin/python -t

# binary search
# time O(n)
# space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            # Case 1: find target
            if nums[mid] == target:
                return mid
            
            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

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

