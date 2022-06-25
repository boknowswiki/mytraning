#!/usr/bin/python3 -t

# binary search
# time O(logn)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        if n == 0:
            return 0

        start = 0
        end = n-1

        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid

        return max(nums[start], nums[end])


if __name__ == '__main__':
    s = Solution()
    a = [1,2,4,8,6,3]
    a = [10, 9, 8]
    a = [1,2,3]
    print(s.mountain_sequence(a))

# binary search same as 0075

# better and cleaner

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        l = 0
        r = n-1
        
        while l+1 < r:
            mid = (l+r)/2
            if nums[mid] < nums[mid+1]:
                l = mid
            else:
                r = mid
                
        return max(nums[l], nums[r])
        

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return nums[mid]
            elif nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid
                
        print l
        return nums[l]

if __name__ == '__main__':
    s = [60]
    ss = Solution()
    print "answer is\n"
    print ss.mountainSequence(s)
