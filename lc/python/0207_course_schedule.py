
# bfs and topological sort
# time O(n)
# space O(n)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        firstTake = {}
        needTake = {}
        for a, b in prerequisites:
            if b not in firstTake:
                firstTake[b] = []
            firstTake[b].append(a)
            if a not in needTake:
                needTake[a] = []
            needTake[a].append(b)
            
        start = []
        for i in range(numCourses):
            if i not in needTake:
                start.append(i)
                
        q = collections.deque(start)
        canTake = set(start)
        
        #print(f"firstTake {firstTake}, needTake {needTake}, start {start}, canTake {canTake}")
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if c in firstTake:
                    for d in firstTake[c]:
                        if c in needTake[d]:
                            needTake[d].remove(c)
                        if len(needTake[d]) == 0 and d not in canTake:
                            q.append(d)
                            canTake.add(d)
                        
        return len(canTake) == numCourses
      
    def canFinish(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n
