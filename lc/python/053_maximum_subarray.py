#!/usr/bin/python -t

#DP time O(n) space O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_ret = nums[0]
        max_sofar = nums[0]

        for i in range(1, n):
            max_sofar = max(nums[i], max_sofar + nums[i])
            max_ret = max(max_ret, max_sofar)
            
        return max_ret
    
# divide and conquer
# time O(nlogn)
# space O(nlogn)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(arr, start, end):
            if start > end:
                return -sys.maxsize-1
            
            mid = (start+end)//2
            total = 0
            left_total = right_total = 0
            for i in range(mid-1, start-1, -1):
                total += arr[i]
                left_total = max(left_total, total)
                
            total = 0
            for i in range(mid+1, end+1):
                total += arr[i]
                right_total = max(right_total, total)
                
            return max(helper(arr, start, mid-1), helper(arr, mid+1, end), left_total+arr[mid]+right_total)
            
        return helper(nums, 0, len(nums)-1)

#DF time O(n) space O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        max_here = nums[0]
        max_sofar = nums[0]

        for i in xrange(1, n):
            max_here = max(max_here+nums[i], nums[i])
            max_sofar = max(max_sofar, max_here)

        return max_sofar


#divide and conquer
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        def divide_conquer(l, r, nums):
            if l > r:
                return -2**32-1

            mid = (l+r)/2
            lan = divide_conquer(mid+1, r, nums)
            ran = divide_conquer(l, mid-1, nums)
            s = 0
            lmax = 0
            for i in range(mid-1, l-1, -1):
                s = s + nums[i]
                lmax = max(s, lmax)

            s = 0
            rmax = 0
            for i in range(mid+1, r+1):
                s = s + nums[i]
                rmax = max(s, rmax)

            return max(lmax+nums[mid]+rmax, lan, ran)


        return divide_conquer(0, n-1, nums)

