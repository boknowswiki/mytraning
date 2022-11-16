# bfs

# referece: https://leetcode.com/problems/water-and-jug-problem/discuss/83709/Breadth-First-Search-with-explanation.

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        v = set((0, 0))
        q = collections.deque([(0, 0)])
        
        while q:
            j1, j2 = q.popleft()
            if j1 + j2 == targetCapacity:
                return True
            
            states = set()
            states.add((j1, 0)) # empty j2
            states.add((0, j2)) # empty j1
            states.add((jug1Capacity, j2)) # fullfil j1
            states.add((j1, jug2Capacity)) # fullfil j2
            states.add((min(jug1Capacity, j1+j2), j2-(jug1Capacity-j1) if j2 > jug1Capacity-j1 else 0)) # pur j2 to j1
            states.add((j1-(jug2Capacity-j2) if j1>jug2Capacity-j2 else 0, min(jug2Capacity, j1+j2))) # pur j1 to j2
            
            for state in states:
                if state not in v:
                    v.add(state)
                    q.append(state)
                    
        return False
