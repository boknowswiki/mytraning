# array
# time O(n)
# space O(1)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []

        for num in nums:
            if not ret:
                ret.append(num)
            else:
                ret.append(num+ret[-1])

        return ret
