#!/usr/bin/python -t


class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    if len(temp) > 0 and temp[-1] > candidates[j]:
                        continue
                    temp.append(candidates[j])
                    dp[i].append(temp)
        return dp[target]


#class Solution(object):
#    def combinationSum(self, candidates, target):
#        """
#        :type candidates: List[int]
#        :type target: int
#        :rtype: List[List[int]]
#        """
#        candidates.sort()
#        return self.get_combi_sum(candidates, [], 0, target)
#    
#    def get_combi_sum(self, candidates, prefix, cur, target):
#        if len(prefix) == 0:
#            max_val = candidates[0]
#        else:
#            max_val = prefix[-1]
#            
#        ret = []    
#        for i in range(len(candidates)):
#            if candidates[i] >= max_val:
#                if cur + candidates[i] == target:
#                    ret.append(prefix + [candidates[i]])
#                elif cur + candidates[i] < target:
#                    ret.extend(self.get_combi_sum(candidates, prefix+[candidates[i]], cur+candidates[i], target))
#                else:
#                    pass
#                
#        return ret

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
