#!/usr/bin/python -t

#time O(n) space O(1)
#myself resolved

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ret = max_pro = min_pro = nums[0]
        
        for i in range(1, n):
            if nums[i] < 0:
                max_pro, min_pro = min_pro, max_pro
                
            max_pro = max(max_pro*nums[i], nums[i])
            min_pro = min(min_pro *nums[i], nums[i])
            ret = max(ret, max_pro)
            
        return ret

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        max_pro = nums[0]
        min_pro = nums[0]
        max_sofar = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                max_pro, min_pro = min_pro, max_pro

            
            max_pro = max(max_pro*nums[i], nums[i])
            min_pro = min(min_pro*nums[i], nums[i])
            max_sofar = max(max_pro, max_sofar)
            print 'max_sofar %d, max_pro %d, min_pro %d' % \
                (max_sofar, max_pro, min_pro)

        return max_sofar



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_v = max_v = ret = nums[0]
        
        
        for i in xrange(1,n):
            if nums[i] < 0:
                max_v, min_v = min_v, max_v
                
            max_v = max(nums[i], max_v * nums[i])
            min_v = min(nums[i], min_v * nums[i])
            ret = max(max_v, ret)
            
        return ret

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.maxProduct([-4,-3,-2])))
