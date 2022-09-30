#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n-1
        
        while l + 1 < r:
            if nums[l] == nums[l+1]:
                l += 1
                continue
            if nums[r] == nums[r-1]:
                r -= 1
                continue
                
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            elif nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid
                    
        if nums[r] == target or nums[l] == target:
            return True
        return False

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


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        l = 0
        r = n - 1
        
        while l <= r:
            m = l + (r-l)/2
            
            if nums[m] == target:
                return True
            
            if nums[m] > nums[l]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m+1
            elif nums[m] < nums[l]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1
            else:
                l = l + 1
                
        return False
        #return False if nums[l] != target else True

