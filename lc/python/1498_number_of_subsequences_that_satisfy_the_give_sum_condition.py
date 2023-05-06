# binary search, sort

# time O(nlogn)
# space O(n)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        nums.sort()
        ret = 0
        
        for i in range(n):
            j = bisect.bisect_right(nums, target-nums[i]) - 1
            if j >= i:
                ret += pow(2, j-i, mod)

        return ret % mod
      
# two pointers, sort

# time O(nlogn)
# space O(1)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10 ** 9 + 7
        ret = 0
        l = 0
        r = n-1

        while l <= r:
            if nums[l] + nums[r] <= target:
                ret = (ret + pow(2, r-l, mod)) % mod
                l += 1
            else:
                r -= 1

        return ret
