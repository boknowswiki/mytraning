#!/usr/bin/python -t

# BFS
#
#搜索。
#将字符串看成一个点的话，对于基因库的任意两个字符串间所需的突变次数作为边权，原题就可以转化为初始串在图中只经过边权为1的边是否能走到结束串的点。


from collections import deque

class Solution:
    """
    @param start: 
    @param end: 
    @param bank: 
    @return: the minimum number of mutations needed to mutate from "start" to "end"
    """
    def minMutation(self, start, end, bank):
        # Write your code here
        if start == end:
            return 0
            
        v_bank = set(bank)
        q = deque()
        q.append((start, 0))
        
        while len(q) > 0:
            g, step = q.popleft()
            
            if g == end:
                return step
                
            for c in "ACGT":
                for i in range(len(g)):
                    new_g = g[:i] + c + g[i+1:]
                    if new_g in v_bank:
                        q.append((new_g, step+1))
                        v_bank.remove(new_g)
                        
        return -1
        
        
