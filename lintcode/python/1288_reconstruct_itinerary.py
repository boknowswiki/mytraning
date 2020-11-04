#!/usr/bin/python -t

# 将从一个机场可以到达的所有机场逆序排序，再DFS找出答案


import collections

class Solution:
    """
    @param tickets: 
    @return: nothing
    """
    def findItinerary(self, tickets):
        # Write your code here
        citys = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            print a, b
            citys[a].append(b)
            
        print citys
        
        ret = []
        
        self.dfs(citys, "JFK", ret)
        
        return ret[::-1]
    
    def dfs(self, cs, c, ret):
        while cs[c]:
            self.dfs(cs, cs[c].pop(), ret)
        print c
        ret.append(c)
        
        return
