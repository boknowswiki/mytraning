# backtracking
# time O(2^m*n)
# space O(m+n)

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        ret = 0

        def dfs(index, count):
            nonlocal ret
            if index == len(requests):
                for i in range(n):
                    if indegree[i] != 0:
                        return

                ret = max(ret, count)

                return

            indegree[requests[index][0]] -= 1
            indegree[requests[index][1]] += 1

            dfs(index+1, count+1)

            indegree[requests[index][0]] += 1
            indegree[requests[index][1]] -= 1

            dfs(index+1, count)

            return
        
        dfs(0, 0)

        return ret
