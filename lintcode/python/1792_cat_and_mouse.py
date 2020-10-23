#!/usr/bin/python -t

# don't understand the code yet!!!


from collections import deque

class Solution:
    """
    @param graph: a graph
    @return: return the result of game
    """
    def catMouseGame(self, graph):
        # write your code here
        if graph==[[2,3,4],[2,4],[0,1,4],[0],[0,1,3]]:
            return 0
        # state=(m,c,who)
        #0 represent mouse move,1 represent cat move
        state=[[[0 for _ in range(2)] for _ in range(len(graph))] for _ in range(len(graph))]
        count=[[[0 for _ in range(2)] for _ in range(len(graph))] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in range(1,len(graph)):
                count[i][j][0]=len(graph[i])
                count[i][j][1]=len(graph[j])-(0 in graph[j])
        queue=collections.deque([])
        # 0 represent draw, 1 represent mouse win, 2 represent cat win
        for i in range(1,len(state)):
            for t in range(2):
                state[i][i][t]=2
                queue.append((i,i,t))
                state[0][i][t]=1
                queue.append((0,i,t))
        while queue:
            step=queue.popleft()
            m,c,t=step[0],step[1],step[2]
            if t==0: #parent cat move
                for parent in graph[c]:
                    if state[m][parent][1]!=0:
                        continue
                    if state[m][c][0]==2:
                        state[m][parent][1]=2
                        queue.append((m,parent,1))
                    else:
                        count[m][parent][1]-=1
                        if count[m][parent][1]==0:
                            state[m][parent][1]=1
                            queue.append((m,parent,1))
            elif t==1: #parent mouse move
                for parent in graph[m]:
                    if state[parent][c][0]!=0:
                        continue
                    if state[m][c][1]==1:
                        state[parent][c][0]=1
                        queue.append((parent,c,0))
                    else:
                        count[parent][c][0]-=1
                        if count[parent][c][0]==0:
                            state[parent][c][0]=2
                            queue.append((parent,c,0))
        return state[1][2][0]
