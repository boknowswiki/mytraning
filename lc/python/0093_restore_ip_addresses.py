# string and backtracking

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4:
            return []

        ret = []

        def dfs(start, path):
            if start == n and len(path) == 4:
                ret.append(".".join(path))
                return

            val = 0
            if not path or len(path) < 4:
                for i in range(start, min(start+4, n)):
                    val = val * 10 + int(s[i])
                    if str(val) == s[start:i+1] and 0 <= val <= 255:
                        path.append(str(val))
                        dfs(i+1, path)
                        path.pop()

        dfs(0, [])

        return ret
