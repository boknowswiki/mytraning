#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
            
        if k > n:
            return sum(nums)
            
        ret = []
        total = 0
        start = 0
        for i in range(n):
            total += nums[i]
            
            if i - start + 1 == k:
                ret.append(total)
                total -= nums[start]
                start += 1
                
        return ret
        


class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        n = len(nums)
        if n < k or k <= 0:
            return []
        sums = [0] * (n - k + 1)
        for i in range(k):
            sums[0] += nums[i];

        for i in range(1, n - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]

        return sums
