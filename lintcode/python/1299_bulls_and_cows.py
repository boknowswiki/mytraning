#!/usr/bin/python -t

# hash table
# 题解：第一遍遍历计算所有相同位置大小相同的个数，分别用大小为10的数组记录两个字符串每个数字出现的次数，第二次遍历数组，相同的次数为对应位置的最小值。

class Solution:
    """
    @param secret: 
    @param guess: 
    @return: nothing
    """
    def getHint(self, secret, guess):
        # 
        a, b, n = 0, 0, len(secret)
        
        ds = [0] * 10
        dg = [0] * 10
        
        for i in range(n):
            x = ord(secret[i]) - ord('0')
            y = ord(guess[i]) - ord('0')
            if x == y:
                a += 1
                
            ds[x] += 1
            dg[y] += 1
            
        for i in range(10):
            b += min(ds[i], dg[i])
            
        return str(a) + "A" + str(b-a) + "B"
        
            
