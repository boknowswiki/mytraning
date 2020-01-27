#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        # write your code here
        m = len(Matrix)
        
        s = set(Matrix[0])
        new_s = set()
        
        for i in range(1, m):
            new_s.clear()
            for j in Matrix[i]:
                if j in s:
                    new_s.add(j)
                    
            s = set(new_s)
           
        #print new_s
        return new_s.pop()
        
        
