class Solution:
    """
    @param nums: an array of integers
    @param threshold: an integer
    @return: return the smallest divisor
    """
    def smallestDivisor(self, nums, threshold):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        nums.sort()
        l = 1
        r = nums[-1]
        
        while l +1< r:
            mid = (l+r)/2
            val = self.getVal(nums, mid)
            #print l, r, mid, val
            if val <= threshold:
                r = mid
            else:
                l = mid
        if self.getVal(nums, l) <= threshold:
            return l
        return r
        
    def getVal(self, nums, target):
        ret = 0
        
        for num in nums:
            ret += num/target
            if num%target != 0:
                ret += 1
                
        return ret
