#!/usr/bin/python -t

# binary search

class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        if m > n:
            return 0
        if m == n:
            return max(nums)
            
        l = max(nums)
        r = sum(nums)
        
        while l +1< r:
            mid = l+(r-l)/2
            cnt = self.helper(nums, mid)
            print l, r, mid, cnt
            if cnt <= m:
                r = mid
            else:
                l = mid
        
        print l, r        
        if self.helper(nums, l) == m:
            return l
        return r
        
    def helper(self, nums, target):
        cnt = 0
        total = 0#nums[0]
        l = 0
        print target
        for i in range(len(nums)):
            total += nums[i]
            if total > target:
                cnt += 1
                total = nums[i]

        print cnt       
        return cnt+1

#!/usr/bin/python -t

# binary search

class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        n = len(nums)
        if n < m or n == 0:
            return 0

        start = max(nums)
        end = sum(nums)

        while start + 1 < end:
            target = (start+end)//2
            if self.target_sum_satisfy_m(nums, m, target):
                end = target
            else:
                start = target
        if self.target_sum_satisfy_m(nums, m, start):
            return start

        return end

    def target_sum_satisfy_m(self, nums, m, target):
        cnt = 0
        curSum = 0

        for num in nums:
            if curSum+num <= target:
                curSum += num
            else:
                curSum = num
                cnt += 1

        cnt+= 1

        return cnt <= m
        


if __name__ == '__main__':
    s = Solution()
    a = [7,2,5,10,8]
    b = 2
    print(s.splitArray(a, b))
