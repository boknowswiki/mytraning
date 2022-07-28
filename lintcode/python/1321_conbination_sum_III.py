#!/usr/bin/python3 -t

# dfs
# time O((m
#         k) * k), m is the size of the numbers, here m is 9. so total (m
#                                                                       k) combinations, and every time, it takes O(k) to check the solution.
# space O(m), the stack takes O(m) to get the solution.

from typing import (
    List,
)

class Solution:
    """
    @param k: an integer
    @param n: an integer
    @return: return a List[List[int]]
    """
    def combination_sum3(self, k: int, n: int) -> List[List[int]]:
        # write your code here
        ret = []

        self.dfs(1, k, n, [], ret)

        return ret

    def dfs(self, start, k, n, path, ret):
        if k == 0 and n == 0:
            ret.append(list(path))
            return
        
        for i in range(start, 10):
            if k > 0 and n - i >= 0:
                path.append(i)
                self.dfs(i+1, k-1, n-i, path, ret)
                path.pop()
            else:
                break

        return


if __name__ == '__main__':
    s = Solution()
    a = 3
    b = 7
    a = 3
    b = 9
    print(s.combination_sum3(a, b))