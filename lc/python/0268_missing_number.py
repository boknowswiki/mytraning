#!/usr/bin/python -t

# sum solution
# time O(n)
# space O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (0 + len(nums)) * (len(nums)+1)//2
        
        for num in nums:
            total -= num
            
        return total
      
# binary search
