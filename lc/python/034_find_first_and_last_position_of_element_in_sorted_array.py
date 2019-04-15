#!/usr/bin/python -t

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

#time O(logn) space O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_index(nums, target):
            n = len(nums)
            start = 0
            end = n - 1
            
            while start < end:
                mid = (start+end)/2
                if nums[mid] >= target:
                    end = mid
                else:
                    start = mid + 1
                    
            if nums[start] == target:
                return start
            else:
                return -1
            
            
        def right_index(nums, target):
            n = len(nums)
            start = 0
            end = n - 1
            
            while start <= end:
                mid = (start+end)/2
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = start + 1
                    
            return end
                
        if len(nums) == 0:
            return [-1, -1]
        l = left_index(nums, target)
        if l == -1:
            return [-1, -1]
        r = right_index(nums, target)
        
        return [l, r]

#time O(nlogn) space O(1)


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        start = 0
        end = n - 1
        ret = [-1, -1]
        
        while start <= end:
            mid = (start+end)/2
            
            if nums[mid] == target:
                l = r = mid
                while l >= 1 and nums[l-1] == target:
                    l = l - 1
                    
                while r <= n-2 and nums[r+1] == target:
                    r = r + 1
                    
                ret = [l, r]
                
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return ret
