#!/usr/bin/python -t

# binary search
# time O(n^2logn)
# space O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
    
# two pointers

#time O(n^2) space O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        if n <= 3:
            return sum(nums)
        
        ret = nums[0] + nums[1] + nums[2]
        
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
                
            while j < k:
                total =nums[i] + nums[j] + nums[k]

                if abs(target - ret) > abs(target-total):
                        ret = total
                if total-target < 0:
                    j = j + 1
                else:
                    k = k - 1
                
        return ret

