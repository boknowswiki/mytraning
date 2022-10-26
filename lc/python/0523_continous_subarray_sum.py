# hash map
# time O(n)
# space O(n)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:0}
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            
            if total % k not in d:
                d[total%k] = i+1
            elif d[total%k] < i:
                return True
            
        return False
