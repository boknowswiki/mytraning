#!/usr/bin/python -t

class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    def openLock(self, deadends, target):
        # Write your code here
        dead = set(deadends)
        if '0000' in dead: return -1
        neighbors = set(self.adjacent(target))
        if neighbors & dead == neighbors: return -1
        visited = set()
        queue = collections.deque(['0000'])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                now = queue.popleft()
                if now == target: return step - 1
                visited.add(now)
                for n in self.adjacent(now):
                    if n in dead or n in visited: continue
                    queue.append(n)
                    visited.add(n)
        return -1
    
    def adjacent(self, now):
        res = []
        for i in range(4):
            left, mid, right = now[:i], int(now[i]), now[i + 1:]
            for m in [(mid + 1) % 10, (mid - 1) % 10]: res.append(left + str(m) + right)
        return res
