#!/usr/bin/python3 -t


# binary search
# time O(n)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recover_rotated_sorted_array(self, nums: List[int]):
        # write your code here
        n = len(nums)
        if n < 2:
            return

        start = 0
        end = n-1

        # find pivot
        while start + 1 < end:
            if nums[start] < nums[end]:
                break

            mid = start + (end-start)//2

            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1

        pivot = start if nums[start] < nums[end] else end

        print(f"{pivot}")
        self.reverse(nums, 0, pivot-1)
        self.reverse(nums, pivot, n-1)
        self.reverse(nums, 0, n-1)

        return
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return


if __name__ == '__main__':
    s = Solution()
    a = [4, 5, 1, 2, 3]
    s.recover_rotated_sorted_array(a)
    print(a)

# binary search
# time O(n) worse case

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i+1, n-1)
                self.reverse(nums, 0, n-1)
                
        return
    
    
    def reverse(self, nums, l, r):
        if l >= r:
            return
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        return
    
