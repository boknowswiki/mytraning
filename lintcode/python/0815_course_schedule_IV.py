#!/usr/bin/python -t

# dfs and topology sort

# 首先， 用拓扑排序的方法建图， 得到graph和in_degree。 注意graph和in_degree其实是2个不同的方法的哦。
# 
# 然后我们开始深搜。 关键点在于找candidates. 和拓扑排序类似的就是， 当degree = 0的时候就成为了candidates。 然后回溯的时候， 需要把减了的indegree再加回去。

import collections

class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        # Write your code here
        graph, pre_cnt = self.build_graph(n, p)
        candidates = []
        for i in range(len(pre_cnt)):
            if pre_cnt[i] == 0:
                candidates.append(i)
        ret = []

        return self.dfs(n, graph, pre_cnt, candidates, set(), ret)

    def dfs(self, n, graph, pre_cnt, candidates, taken, ret):
        if len(taken) == n:
            return 1

        total_cnt = 0
        for candidate in candidates:
            if candidate in taken:
                continue
            taken.add(candidate)
            new_candidates = []
            for new_c in graph[candidate]:
                pre_cnt[new_c] -= 1
                if pre_cnt[new_c] == 0:
                    new_candidates.append(new_c)
            cnt = self.dfs(n, graph, pre_cnt, candidates+new_candidates, taken, ret)
            total_cnt += cnt
            for new_c in graph[candidate]:
                pre_cnt[new_c] += 1
            taken.remove(candidate)

        return total_cnt


    def build_graph(self, n, p):
        graph = collections.defaultdict(list)
        pre_cnt =[0]*n

        for pre in p:
            pre_cnt[pre[1]] += 1
            graph[pre[0]].append(pre[1])

        return graph, pre_cnt
