#!/usr/bin/python -t

# two pointers

# time O(n) space O(n)

class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        if len(nums) < 2 or k <0:
            return 0
        ret=0
        if k == 0:
            counter = {}
            for num in nums:
                if num not in counter:
                    counter[num] = 0
                counter[num] += 1
                if counter[num] == 2:
                    ret += 1
            return ret
        
        nums = set(nums)
        for num in nums:
            if num+k in nums:
                ret += 1
        return ret
        

# time O(logn) space O(1)

class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        n = len(nums)
        ret = 0
        nums.sort()
        left = 0
        right = 0
        
        while right < n:
            if left == right:
                right += 1
            while left+1 < n and nums[left] == nums[left+1]:
                left += 1
                
            while right + 1 < n and nums[right] == nums[right+1]:
                right += 1
            
            if right >= n:
                break
            
            while right + 1 < n and abs(nums[right] - nums[left]) < k:
                right += 1
                
            if abs(nums[right] - nums[left]) == k:
                ret += 1
                right += 1

            left += 1
            
        return ret
        
