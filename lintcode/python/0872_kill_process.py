#!/usr/bin/python -t

# BFS

from collections import deque

class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        
        mapping = {}
        
        for i, parent in enumerate(ppid):
            if parent not in mapping:
                mapping[parent] = []
            mapping[parent].append(pid[i])
            
        q = deque([kill])
        ret = []
        
        while len(q) > 0:
            p = q.popleft()
            #print p, mapping
            ret.append(p)
            #print ret, type(p)
            if p in mapping:
                q += mapping[p]
                
        return ret

# DFS

class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        n = len(pid)
        child = {}
        for i in range(n):
            if ppid[i] not in child:
                child[ppid[i]] = []
            child[ppid[i]].append(pid[i])

        ans = []
        self.dfs(kill, ans, child)
        return ans

    def dfs(self, now, ans, child):
        ans.append(now)
        if now in child:
            for nxt in child[now]:
                self.dfs(nxt, ans, child)
        

if __name__ == '__main__':
    s = [1,3,10,5]
    v = [3,0,5,3]
    k = 5
    ss = Solution()
    print "answer is\n"
    print ss.killProcess(s, v, k)
