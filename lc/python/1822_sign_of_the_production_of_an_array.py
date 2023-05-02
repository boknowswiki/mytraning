# array, math
# time O(n)
# space O(1)

class Solution(object):
    def arraySign(self, nums):
        countNegativeNumbers = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                countNegativeNumbers = countNegativeNumbers + 1

        if countNegativeNumbers %2 == 0:
            return 1
        return -1
      
class Solution(object):
    def arraySign(self, nums):
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -1 * sign

        return sign

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for num in nums:
            p *= num

        return 1 if p > 0 else -1 if p < 0 else 0
