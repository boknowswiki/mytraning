
class Solution:
    """
    @param nums: a list of integers
    @param k: a integer
    @return: return a integer
    """
    def smallestDistancePair(self, nums, k):
        # write your code here
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        while start + 1 < end:
            mid = (end - start)/2 + start

            if self.count(mid, nums) >= k:
                end = mid
            else:
                start = mid
                
        if self.count(start, nums) >= k:
            return start
        return end
            
    def count(self, mid, nums):
        count = 0
        import bisect
        for i in range(len(nums)):
            count += i - bisect.bisect_left(nums, nums[i] - mid)
        return count
