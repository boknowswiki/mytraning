#!/usr/bin/python -t

# DFS, could be solve in BFS too

class Solution:
    """
    @param relationship: the relationship
    @return: the organization chart
    """

    def dfs(self ,root, ans, manager, Next, time, num, dep):
        res = ''
        for i in range(dep):
            res += '-'
        res += root + ' (' + manager[root] + ') ' + time[root]
        ans.append(res)
    
        for x in Next[num[root]]:
            self.dfs(x, ans, manager, Next, time, num, dep+1)

    def getOrganization(self, relationship):
        # Write your code here
        manager = {}
        time = {}
        num = {}
        Next = []
        ans = []
        root = ''
        
        # Init
        for i in range(len(relationship)):
            manager[relationship[i][0]] = relationship[i][2]
            time[relationship[i][0]] = relationship[i][3]
            num[relationship[i][0]] = i
            Next.append([])
        
        # Build the Tree of relations
        for i in range(len(relationship)):
            if relationship[i][1] == 'NULL':
                root = relationship[i][0]
            else:
                v = num[relationship[i][1]]
                Next[v].append(relationship[i][0])
        #print Next
        
        for i in range(len(relationship)):
            Next[i].sort()
        #print Next
        #print num
        self.dfs(root, ans, manager, Next, time, num, 0)
        return ans
        
        
