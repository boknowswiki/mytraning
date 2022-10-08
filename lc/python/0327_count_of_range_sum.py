
# presum, merge sort
# time O(nlogn)
# space O(n)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
            
        def sort(lo, hi):
            mid = lo + (hi-lo)//2
            if mid == lo:
                return 0
            cnt = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            
            # this is to find any sum val cross left and right, since only in left, and only in right are returned from line 16.
            for val in pre_sum[lo:mid]:
                while i < hi and pre_sum[i] - val < lower:
                    i += 1
                while j < hi and pre_sum[j] - val <= upper:
                    j += 1
                cnt += j-i
                
            pre_sum[lo:hi] = sorted(pre_sum[lo:hi])
            
            return cnt
            
            
        return sort(0, len(pre_sum))
