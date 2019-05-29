#!/usr/bin/python -t

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = n + 1
        
        ss = [0]*(n+1)
        
        for i in xrange(1, n+1):
            ss[i] = ss[i-1] + nums[i-1]
        
        for i in xrange(1, n+1):
            to_find = s + ss[i-1]
            bound = bisect.bisect_left(ss, to_find)
            if bound != len(ss):
                ret = min(ret, bound-i+1)
            
        return 0 if ret == n+1 else ret

#time O(n) space O(1)

#http://www.martinbroadhurst.com/binary-search-in-python.html

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_val = left = 0
        ret = n+1
        for right, i in enumerate(nums):
            sum_val = sum_val + i
            while sum_val >= s:
                ret = min(ret, right-left+1)
                sum_val = sum_val - nums[left]
                left = left + 1
                
                
        return 0 if ret > n else ret


#time O(nlogn) space O(n)
class Solution:

def minSubArrayLen(self, target, nums):
    result = len(nums) + 1
    for idx, n in enumerate(nums[1:], 1):
        nums[idx] = nums[idx - 1] + n
    left = 0
    for right, n in enumerate(nums):
        if n >= target:
            left = self.find_left(left, right, nums, target, n)
            result = min(result, right - left + 1)
    return result if result <= len(nums) else 0

def find_left(self, left, right, nums, target, n):
    while left < right:
        mid = (left + right) // 2
        if n - nums[mid] >= target:
            left = mid + 1
        else:
            right = mid
    return left
