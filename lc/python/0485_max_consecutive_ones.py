# array
# time O(n)
# space O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        cnt = 0

        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1

            ret = max(ret, cnt)

        return ret
