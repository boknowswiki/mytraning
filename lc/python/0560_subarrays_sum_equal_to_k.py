
# presum and hashmap
# time O(n)
# space O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 and k == 0:
            return 1
        if n == 1:
            if nums[0] == k:
                return 1
            return 0
        
        d = {0:1}
        pre_sum = 0
        cnt = 0
        for num in nums:
            pre_sum += num
            cnt += d.get(pre_sum-k, 0)
            d[pre_sum] = d.get(pre_sum, 0) + 1
            
        return cnt

# presum # exceed time limited
# time O(n^2)
# space O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 and k == 0:
            return 1
        if n == 1:
            if nums[0] == k:
                return 1
            return 0
        
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        #print(f"pre_sum {pre_sum}")

        cnt = 0

        for r in range(1, len(pre_sum)):
            for l in range(r):
                if pre_sum[r] - pre_sum[l] == k:
                    cnt += 1

        return cnt
