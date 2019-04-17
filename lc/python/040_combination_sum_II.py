#!/usr/bin/python -t


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # check if this number is used
                    if len(temp) > 0 and temp[-1] >= j:
                        continue
                    # store index
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check = {}
        for temp in dp[target]:
            value = [candidates[t] for t in temp]
            try:
                check[str(value)] += 1
            except KeyError:
                check[str(value)] = 1
                res.append(value)
        return res


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []
        self.get_combi_sum(candidates, 0, [], ret, target)
        return ret
    
    def get_combi_sum(self, candidates, start, path, ret, target):
        if not target:
            ret.append(path)
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if target < candidates[i]:
                break
            self.get_combi_sum(candidates, i+1, path + [candidates[i]], ret, target-candidates[i])

