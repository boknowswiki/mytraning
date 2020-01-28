#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param imput: 
    @param id: 
    @return: the total importance value 
    """
    def getImportance(self, imput, id):
        # Write your code here.
        d = {}
        imput = eval(imput)
        
        def dfs(id):
            cnt = d[id][0]
            for e in d[id][1]:
                cnt += dfs(e)
                
            return cnt
                
        
        for e in imput:
            #print e
            d[e[0]] = [e[1], e[2]]
            
        #print d
        
        return dfs(id) if id in d else 0
        
