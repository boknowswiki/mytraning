#!/usr/bin/python -t

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
