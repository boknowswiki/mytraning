#!/usr/bin/python3 -t

# iterative way

class Solution:
    """
    @param s: a string
    @return: return a list of strings
    """
    def letter_case_permutation(self, s: str) -> List[str]:
        # write your code here
        result = [s]
        for i in range(len(s)):
            if s[i].isdigit():
                continue
            size = len(result)
            for j in range(size):
                tmp = [ch for ch in result[j]]
                tmp[i] = tmp[i].lower() if tmp[i].isupper() else tmp[i].upper()
                result.append("".join(tmp))
        return result

# dfs
# time O(2^mn)
# space O(2^mn)

from typing import (
    List,
)

class Solution:
    """
    @param s: a string
    @return: return a list of strings
             we will sort your return value in output
    """
    def letter_case_permutation(self, s: str) -> List[str]:
        # write your code here
        n = len(s)
        if n == 0:
            return [""]

        ret = []

        self.dfs(s, 0, ret)

        return ret

    def dfs(self, s, index, ret):
        ret.append(s)
        
        for i in range(index, len(s)):
            if not s[i].isdigit():
                if s[i].isupper():
                    self.dfs(s[:i] + s[i].lower() + s[i+1:], i+1, ret)
                else:
                    self.dfs(s[:i] + s[i].upper() + s[i+1:], i+1, ret)

        return

if __name__ == '__main__':
    s = Solution()
    a = "a1b2"
    print(s.letter_case_permutation(a))
    
