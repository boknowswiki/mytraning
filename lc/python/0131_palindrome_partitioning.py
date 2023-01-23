# dfs and backtracking
# time O(n* 2^n)
# space O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = []

        def dfs(start, path):
            if start == n:
                ret.append(list(path))
                return
            
            for i in range(start, n):
                sub_s = s[start:i+1]
                if self.is_palindrome(sub_s):
                    path.append(sub_s)
                    dfs(i+1, path)
                    path.pop()

            return

        dfs(0, [])

        return ret

    def is_palindrome(self, a):
        l = 0
        r = len(a)-1

        while l < r:
            if a[l] != a[r]:
                return False

            l += 1
            r -= 1

        return True
