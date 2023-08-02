# dfs, backtracking
# time O(n*n!)
# space O(n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        if n == 0:
            return [[]]
        if n == 1:
            return [nums]

        def dfs(path):
            nonlocal n, ret, nums
            if len(path) == n:
                ret.append(list(path))
                return

            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(path)
                    path.pop()


        dfs([])

        return ret
