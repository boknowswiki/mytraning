# array
# time O(mn)
# space O(1)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        if n == 0:
            return 0

        ret = sum(accounts[0])

        for i in range(1, n):
            ret = max(ret, sum(accounts[i]))

        return ret
