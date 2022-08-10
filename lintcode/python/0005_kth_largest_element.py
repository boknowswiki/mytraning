#!/usr/bin/python3 -t

# quick select
# time O(n)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        if n == 0 or n < k:
            return 0

        return self.quick_select(nums, 0, n-1, k-1)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        part = self.partition(nums, start, end)
        #print(f"{nums}, {part}")
        if part == k:
            return nums[part]
        elif part < k:
            return self.quick_select(nums, part+1, end, k)
        else:
            return self.quick_select(nums, start, part-1, k)


    def partition(self, nums, start, end):
        pivot = nums[end]

        i = start

        for j in range(start, end):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[end] = nums[end], nums[i]

        return i




if __name__ == '__main__':
    s = Solution()
    a = 1
    b = [1,3,4,2]
    print(s.kth_largest_element(a, b))

# quick select
# similar to 0461

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        l = len(nums)
        if n > l:
            return 0
            
        ret = self.quickselect(nums, 0, l-1, n-1)
        
        return ret
        
        
    def quickselect(self, nums, start, end, k):
        if start == end:
            return nums[start]
            
        part = self.partition(nums, start, end)
        
        #print nums
        
        if part == k:
            return nums[part]
        elif part < k:
            return self.quickselect(nums, part+1, end, k)
        else:
            return self.quickselect(nums, start, part-1, k)
        
        
    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        
        while start < end:
            if nums[start] >= pivot:
                nums[i], nums[start] = nums[start], nums[i]
                i += 1
            start += 1
            
        nums[i], nums[end] = nums[end], nums[i]
        
        return i

