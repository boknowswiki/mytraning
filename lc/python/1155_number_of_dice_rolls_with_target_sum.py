
#dfs with memorization

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        
        def dfs(dice_cnt, need):
            if dice_cnt == 0:
                return 0 if need != 0 else 1
            
            if (dice_cnt, need) in memo:
                return memo[(dice_cnt, need)]
            
            cnt = 0
            for i in range(1, k+1):
                cnt += dfs(dice_cnt-1, need-i)
                
            memo[(dice_cnt, need)] = cnt
            
            return cnt
        
        return dfs(n, target) % (10**9+7)


# dfs, but Time Limit Exceeded

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dfs(dice_cnt, need):
            if dice_cnt == 0:
                return 0 if need != 0 else 1
            
            cnt = 0
            for i in range(1, k+1):
                cnt += dfs(dice_cnt-1, need-i)
                
            return cnt
        
        return dfs(n, target)
