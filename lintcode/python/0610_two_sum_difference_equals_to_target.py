#!/usr/bin/python -t

# two pointers
# time O(n^2)
# space O(1)


from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        n = len(nums)
        if n < 2:
            return [-1, -1]

        ret = [-1, -1]

        nums.sort()

        for i in range(n-1):
            r = n-1

            while i < r:
                if abs(nums[r] - nums[i]) == abs(target):
                    ret = [nums[i], nums[r]]
                    return ret
                elif nums[r] - nums[i] > abs(target):
                    r -= 1
                else:
                    break

        return ret

# two pointers

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        n = len(nums)
        ret = []
        
        nums = sorted(nums, key=lambda x:x[0])
        
        #print nums
        j = 0
        for i in range(n):
            if i == j:
                j += 1
                
            #print i, j
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
                
            if j < n and nums[j][0] - nums[i][0] == target:
                ret = [nums[i][1]+1, nums[j][1]+1]
                
        #print ret
        if ret[0] > ret[1]:
            ret[0], ret[1] = ret[1], ret[0]
                
        return ret
            
