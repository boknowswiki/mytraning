#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param votes: The array of names of candidates in the election.
    @return: The name of the candidate who has the most votes.
    """
    def candidateWithTheMostVotes(self, votes):
        # Write your code here
        d = {}
        ret = ""
        max_cnt = 0
        
        for v in votes:
            d[v] = d.get(v, 0) + 1
            if d[v] >= max_cnt:
                max_cnt = d[v]
               
        for k, v in d.items():
            if v == max_cnt and (k < ret or len(ret) == 0):
                ret = k
                
        return ret
        
