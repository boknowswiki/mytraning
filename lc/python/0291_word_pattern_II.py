# dfs and backtracking and hash map

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        found = dict()
        v = set()

        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True
            if i >= len(pattern) or j >= len(s):
                return False

            if pattern[i] not in found:
                for length in range(1, len(s)-j+1):
                    if s[j:j+length] not in v:
                        v.add(s[j:j+length])
                        found[pattern[i]] = s[j:j+length]
                        if dfs(i+1, j+length):
                            return True
                        v.remove(s[j:j+length])
                        del found[pattern[i]]
            else:
                if s[j:j+len(found[pattern[i]])] == found[pattern[i]]:
                    if dfs(i+1, j+len(found[pattern[i]])):
                        return True
            return False

        return dfs(0, 0)
