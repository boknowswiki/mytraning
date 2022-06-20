#!/usr/bin/python -t


# binary search
# time O(logn)
# space O(1)


from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        if n == 0:
            return -1

        start = 0
        end = n-1

        while start + 1 < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = start + (end-start)//2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])


# binary search solution

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if nums[l] > nums[r]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                return nums[l]
                
        return nums[l]

if __name__ == '__main__':
    s = [1,2,3]
    s = [4,1,2,3]
    s = [4,5,6,7,8,9,1,2,3]
    ss = Solution()
    print "answer is\n"
    print ss.findMin(s)
