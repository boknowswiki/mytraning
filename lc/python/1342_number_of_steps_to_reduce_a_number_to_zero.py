# math
# time O(n)
# space O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ret = 0

        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            ret += 1

        return ret
