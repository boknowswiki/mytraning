# backtrack
# time O(k^n)
# space O(k+n)

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dis_array = [0] * k
        n = len(cookies)

        def dfs(i, child_left):
            if n-i < child_left:
                return sys.maxsize

            if i == n:
                return max(dis_array)

            ret = sys.maxsize

            for j in range(k):
                child_left -= int(dis_array[j] == 0)
                dis_array[j] += cookies[i]

                ret = min(ret, dfs(i+1, child_left))

                dis_array[j] -= cookies[i]
                child_left += int(dis_array[j]==0)

            return ret


        return dfs(0, k)
