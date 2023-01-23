# hash map
# time O(n)
# space O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in trust:
            graph[a].append(b)

        ret = -1
        for i in range(1, n+1):
            if i not in graph:
                ret = i
        
        if ret == -1:
            return ret
        
        for i in range(1, n+1):
            if i == ret:
                continue
            if ret not in graph[i]:
                return -1

        return ret
      
def findJudge(self, N: int, trust: List[List[int]]) -> int:
    
    if len(trust) < N - 1:
        return -1
    
    indegree = [0] * (N + 1)
    outdegree = [0] * (N + 1)
    
    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1
        
    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i
    return -1
  
  def findJudge(self, N: int, trust: List[List[int]]) -> int:

    if len(trust) < N - 1:
        return -1

    trust_scores = [0] * (N + 1)

    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1
    
    for i, score in enumerate(trust_scores[1:], 1):
        if score == N - 1:
            return i
    return -1
