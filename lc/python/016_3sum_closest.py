#!/usr/bin/python -t

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
            return sum(i for i in nums)
        
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

