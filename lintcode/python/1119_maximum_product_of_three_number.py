#!/usr/bin/python -t

# 我们将数组从小到大排序后，
# 1、假设数组元素全为负数或只有一个负数或全为正数，此时将数组中最大的三个元素相乘即为最大乘积；
# 2、假设只有一个正数或两个正数，此时将数组的前两个负数与最后一个正数相乘即为最大乘积；
# 3、假设正数多于三个且负数多于两个，则最大乘积应为前两个负数与最后一个正数的乘积与最大的三个元素的乘积中的最大值。

class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        # Write your code here
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
