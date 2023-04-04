
# greedy

class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count

# dfs

class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        self.ret = n

        def helper(index, level):
            nonlocal n, s
            #print(f"index {index}, char {s[index]}, level {level}")

            if index == n-1:
                self.ret = min(self.ret, level)
                return

            v = set()
            for i in range(index, n):
                if s[i] not in v:
                    v.add(s[i])
                    if i == n-1:
                        self.ret = min(self.ret, level)
                else:
                    helper(i, level+1)
                    break
            return 
        helper(0, 1)
        return self.ret
