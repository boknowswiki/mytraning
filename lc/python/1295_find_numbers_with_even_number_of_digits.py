# array
# time O(n)
# space O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0

        for num in nums:
            cnt = 0
            while num:
                num //= 10
                cnt += 1

            if cnt % 2 == 0:
                ret += 1

        return ret
