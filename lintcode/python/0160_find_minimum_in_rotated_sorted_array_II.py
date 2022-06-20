#!/usr/bin/python3 -t


# binary search
# time O(logn), worst case O(n)
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
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1

        return min(nums[start], nums[end])


if __name__ == '__main__':
    s = Solution()
    a = [4,4,5,6,7,0,1,2]
    a = [1,1,-1,1]
    print(s.find_min(a))

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
            elif nums[l] < nums[r]:
                return nums[l]
            else:
                l += 1
                
        return nums[l]

if __name__ == '__main__':
    s = [1,2,3]
    s = [2,1]
    s = [4,4,5,6,7,0,1,2]
    ss = Solution()
    print "answer is\n"
    print ss.findMin(s)
