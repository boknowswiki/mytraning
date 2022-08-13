#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        nums.sort()
        
        l = 0
        r = n-1
        cnt = 0
        
        while l < r:
            while l < r and nums[l] + nums[r] < target:
                l += 1
                
            if l != r and nums[l] + nums[r] == target:
                cnt += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                    
            r -= 1
            
        return cnt
        

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        n = len(nums)
        nums.sort()
        
        l = 0
        r = n-1
        ret = 0
        
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                l += 1
                r -= 1
                ret += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif val < target:
                l += 1
            else:
                r -= 1

        return ret
        
        
# hash table
# time O(n)
# space O(n)

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        cnt = 0

        for num in num_map:
            if num <= target//2 and target-num in num_map:
                if num == target-num and num_map[num] >= 2:
                    cnt += 1
                if num != target-num:
                    cnt += 1

        return cnt
