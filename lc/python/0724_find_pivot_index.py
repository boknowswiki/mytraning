# array, prefix sum
# time O(n)
# space O(1)

class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
      
# time O(n)
# space O(n)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n+1)

        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        for i in range(n):
            if pre_sum[i] == pre_sum[n] - pre_sum[i]-nums[i]:
                return i

        return -1
