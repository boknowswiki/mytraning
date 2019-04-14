#!/usr/bin/python -t

#time O(logn) space O(1)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start+end)/2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[start]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start = start + 1
                
        return False
