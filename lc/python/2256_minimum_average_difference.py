# presum
# time O(n)
# space O(n)

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        pre_sum = [0] * (n+1)
        for i in range(n):
            pre_sum[i+1] = nums[i] + pre_sum[i]
            
        total = sum(nums)
        ret = n
        min_avg = sys.maxsize
        #print(f"{pre_sum}")
        
        for i in range(n):
            pre_avg = pre_sum[i+1] // (i+1)
            if i != n-1:
                after_avg = (total - pre_sum[i+1]) // (n-i-1)
            else:
                after_avg = 0
            #print(f"i {i}, abs {pre_avg - after_avg}")
            if abs(pre_avg - after_avg) < min_avg:
                min_avg = abs(pre_avg - after_avg)
                ret = i
                
        return ret
