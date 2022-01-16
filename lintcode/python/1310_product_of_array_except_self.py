#!/usr/bin/python3 -t

# prefix sum array presum and array

class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return []

        ret = [1] * n

        pre, post = 1, 1

        for i in range(n):
            ret[i] *= pre
            pre *= nums[i]

        for i in range(n-1, -1, -1):
            ret[i] *= post
            post *= nums[i]

        return ret
        
        
if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4]
    print(s.productExceptSelf(a))