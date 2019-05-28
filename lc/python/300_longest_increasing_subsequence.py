#!/usr/bin/python -t

#binary search, time O(nlogn) space O(n)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ret = 0
        l = []
        
        for i in nums:
            index = bisect.bisect_left(l, i)
            if index >= len(l):
                l.append(i)
            else:
                l[index] = i
                
        return len(l)

#DP, time O(n^2) space O(n)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        l = [0]*n
        l[0] = 1
        ret = 0
        
        for i in range(n):
            max_val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, l[j])
                    
            l[i] = max_val + 1
            ret = max(ret, l[i])
            
        return ret

if __name__ == '__main__':
    s = Solution()
    ss = [10,9,2,5,3,7,101]
    print 'ret %d\n' % s.lengthOfLIS(ss)
