#!/usr/bin/python -t

# hash table
# 只遍历一次的解答
# 只需要在每次 count == 1 的时候加一次兔子的数目，并在count == answers[i] + 1 的时候将answer[i]的计数归零。

class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell 
    @return: the minimum number of rabbits that could be in the forest.
    """
    def numRabbits(self, answers):
        # write your code here
        res = 0 
        count = {}
        for a in answers:
            count[a] = count.get(a, 0) + 1  
            
            if count[a] == 1:
                res += a + 1 
            
            if count[a] == a + 1:
                count[a] = 0 
                
        return res
        
