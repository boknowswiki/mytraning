#!/usr/bin/python -t

# 首先两两枚举判断两个字符串是否相似，遍历找到两个不同的位置，然后将其交换后判断是否相等。
# 利用并查集合并相似的字符串
# 最后，查找并查集中集合的个数即题目要的答案

class Solution:
    def numSimilarGroups(self, A):
        def dfs(s):
            v.add(s)
            for n in edges[s]:
                if n not in v:
                    dfs(n)
            return
        
        ret, edges, v = 0, {}, set()
        
        if len(A) >= 2 * len(A[0]):
            aset = set(A)
            for s in A:
                if s not in edges:
                    edges[s] = set()
                    
                for i in range(len(s)-1):
                    for j in range(i+1, len(s)):
                        new_s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                        if new_s in aset:
                            edges[s].add(new_s)
                            if new_s in edges:
                                edges[new_s].add(s)
                            else:
                                edges[new_s] = {s}
        else:
            for s in A:
                if s not in edges:
                    edges[s] = set()
                for t in A:
                    if s != t:
                        same = 0
                        for i, c in enumerate(t):
                            if c == s[i]:
                                same += 1
                        if same == len(s) - 2:
                            edges[s].add(t)
                            if t in edges:
                                edges[t].add(s)
                            else:
                                edges[t] = {s}
        for s in A:
            if s not in v:
                ret += 1
                dfs(s)
                
        return ret
        
