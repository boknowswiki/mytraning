#!/usr/bin/python -t

# binary search same as 0075

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
