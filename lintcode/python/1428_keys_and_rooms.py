#!/usr/bin/python -t

#有向图的遍历
#先用 BFS 来遍历。使用一个 HashSet 来记录访问过的房间，先把0放进去，然后使用 queue 来辅助遍历，同样将0放入。
#之后进行 BFS 遍历，取出队首的房间，然后遍历其中的所有钥匙，若该钥匙对应的房间已经遍历过了，直接跳过，否则就将钥匙加入 HashSet。
#如果 HashSet 中的钥匙数已经等于房间总数了，表示所有房间已经访问过了，返回 true；否则就将钥匙加入队列继续遍历。
#最后遍历结束后，就看 HashSet 中的钥匙数是否和房间总数相等即可


import collections

class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def canVisitAllRooms(self, rooms):
        # Write your code here
        q = collections.deque([0])
        v = set()
        v.add(0)
        
        while q:
            if len(v) == len(rooms):
                return True
            
            r = q.popleft()
            for key in rooms[r]:
                if key not in v:
                    v.add(key)
                    q.append(key)
                
        return len(v) == len(rooms)
