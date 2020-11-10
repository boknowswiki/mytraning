#!/usr/bin/python -t

# 搜索
# 题解：基本思路就是搜索，c数组统计自己各类球的数量，对board进行遍历，然后j保存一段的起点，i向后移动至出现不同的球，然后对这段长度判断，根据inc判断需要几个球插入，对应的球数量减少，然后截取起点至j的区间和i至区间终点的两段拼接，继续搜索即可。

class Solution:
    """
    @param board: the given board
    @param hand: the balls in your hand
    @return: the minimal balls you have to insert to remove all the balls on the table
    """
    def findMinStep(self, board, hand):
        # Write your code here
        ball = [0 for _ in range(200)]
        for i in range(len(hand)):
            ball[ord(hand[i])] += 1
            
        return self.dfs(board, ball)
        
    def dfs(self, s, b):
        if s == "":
            return 0
            
        ret = len(s) * 2 +1
        i = 0
        
        while i < len(s):
            j = i
            i += 1
            while i < len(s) and s[i] == s[j]:
                i += 1
                
            inc = 3 - i + j
            if b[ord(s[j])] >= inc:
                used = 0 if inc <= 0 else inc
                b[ord(s[j])] -= used
                tmp = self.dfs(s[0:j]+ s[i:], b )
                if tmp >= 0:
                    ret = min(ret, used + tmp)
                    
                b[ord(s[j])] += used
                
        return -1 if ret == 2*len(s)+1 else ret
