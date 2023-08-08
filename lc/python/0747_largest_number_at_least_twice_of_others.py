# array
# time O(n)
# space O(1)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1

        max_val = nums[0]
        max_index = 0

        for i in range(1, n):
            if nums[i] > max_val:
                max_val = nums[i]
                max_index = i

        for i in range(n):
            if nums[i] < max_val:
                if nums[i]*2 > max_val:
                    return -1
        
        return max_index
