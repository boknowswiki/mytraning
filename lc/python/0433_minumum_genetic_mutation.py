# bfs
# time O(n*len(max(word)))
# space O(n)

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        
        ret = 0
        q = collections.deque([start])
        v = {start}
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return ret
                
                for g in bank:
                    if g not in v and self.is_valid(cur, g):
                        q.append(g)
                        v.add(g)
                        
            ret += 1
            
        return -1
    
    def is_valid(self, cur, g):
        if len(cur) != len(g):
            return False
        
        cnt = 0
        
        for i in range(len(cur)):
            if cur[i] != g[i]:
                cnt += 1
                
            if cnt > 1:
                return False
            
        return True
