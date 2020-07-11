#!/usr/bin/python -t

# time O(n)
# 从左到右扫一遍，不满足条件的交换就好了。
# 需要证明的是，当我们 交换了 nums[i] 和 nums[i - 1] 以后：
# 
# ... nums[i - 2], nums[i], nums[i - 1]
# nums[i - 2] 不会和 nums[i] 形成逆序（不满足条件的大小关系）
# 
# 那假如原来是 nums[i - 2] <= nums[i - 1]，那么 nums[i - 1] 和 nums[i] 交换的条件是，nums[i - 1] <= nums[i]。
# 那我们就推导出此时 nums[i] >= nums[i - 2]，因此交换之后，不会让 nums[i] 和 nums[i - 2] 的大小关系出现变化。
# 
# 反过来如果 nums[i - 2] >= nums[i - 1] 的情况同理。
# 
# 或者, 老老实实快排(不需要额外空间的 nlogn 的排序算法), 然后从第2个数开始两两交换.

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        n = len(nums)
        if n < 2:
            return
        
        for i in range(1, n):
            should_swap = nums[i] < nums[i-1] if i%2 else nums[i] > nums[i-1]
            if should_swap:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                
        return
    

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        n = len(nums)
        if n < 2:
            return
        
        self.quicksort(nums, 0, n-1)
        
        for i in range(1, n-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return
    
    def quicksort(self, nums, start, end):
        if start < end:
            part = self.partition(nums, start, end)
        
            self.quicksort(nums, start, part-1)
            self.quicksort(nums, part+1, end)
        
        return
    
    def partition(self, nums, start, end):
        pivot = nums[end]
        index = start
        
        while start < end:
            if nums[start] < pivot:
                nums[index], nums[start] = nums[start], nums[index]
                index += 1
            start += 1
            
        nums[index], nums[end] = nums[end], nums[index]
        
        return index

