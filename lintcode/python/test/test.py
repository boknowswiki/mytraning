#!/usr/bin/python -t

# trie

# 解题思路
# 运用trie的技巧记录下来当前所有数的二进制表示。对于每个数， 他在数组里的最大异或可以通过trie的查询得到。
# 
# 时间复杂度。
# 建立trie O（n times 32）
# 查询trie O（n times 32）

from typing import (
    List,
)

class trieNode:
    def __init__(self):
        self.one = None
        self.zero = None

class trie:
    def __init__(self):
        self.root = trieNode()

    def insert(self, num):
        cur = self.root
        for i in range(32)[::-1]:
            bit = (num>>i) & 1
            if bit == 1:
                if not cur.one:
                    cur.one = trieNode()
                cur = cur.one
            else:
                if not cur.zero:
                    cur.zero = trieNode()
                cur = cur.zero
        return
        

class Solution:
    """
    @param nums: 
    @return: the maximum result of ai XOR aj, where 0 ≤ i, j < n
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Write your code here
        t = trie()
        for num in nums:
            t.insert(num)

        ret = 0
        for num in nums:
            cur = t.root
            val = 0
            for i in range(32)[::-1]:
                bit = (num>>i) & 1
                val *= 2
                if bit == 1:
                    if cur.zero:
                        cur = cur.zero
                        val += 1
                    else:
                        cur = cur.one
                else:
                    if cur.one:
                        cur = cur.one
                        val += 1
                    else:
                        cur = cur.zero
            ret = max(ret, val)

        return ret


if __name__ == '__main__':
    s = Solution()
    a = [3, 10, 5, 25, 2, 8]
    print(s.findMaximumXOR(a))