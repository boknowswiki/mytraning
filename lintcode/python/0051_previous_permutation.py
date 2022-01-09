#!/usr/bin/python -t

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return []
        
        length = len(nums)
        i = length - 1
        
        #找到离结尾最近的一个底点
        while i > 0 and nums[i] >= nums[i - 1]:
            i -= 1

        #print(i)
        
        #这种情况说明list已经是完全递增，直接翻转就可以
        if i == 0:
            return list(reversed(nums))
        
        #找到底点右边比nums[i - 1]小的数字中最大的一个
        j = length - 1
        while nums[j] >= nums[i - 1]:
            j -= 1
        
        print(i, nums[i-1], j)
        #交换两个数字，翻转底点之后的部分
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        return nums[:i] + list(reversed(nums[i:]))       


if __name__ == '__main__':
    s = Solution()
    a = [1,5,2,4,3]

    print(s.previousPermuation(a))