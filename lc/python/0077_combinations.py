# dfs
# time O( (k−1)!⋅(n−k)!/n!)
# space O(k)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def dfs(start, path):
            nonlocal ret, n, k

            if len(path) == k:
                ret.append(list(path))
                return

            for i in range(start, n+1):
                path.append(i)
                dfs(i+1, path)
                path.pop()

            return

        dfs(1, [])

        return ret

  class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)
            remain = n - first_num + 1
            available = remain - need
            
            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

            return
        
        ans = []
        backtrack([], 1)
        return ans
