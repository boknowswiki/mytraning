#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param people: The i-th person has weight people[i].
    @param limit: Each boat can carry a maximum weight of limit.
    @return: Return the minimum number of boats to carry every given person. 
    """
    def numRescueBoats(self, people, limit):
        # Write your code here.
        people.sort()
        
        n = len(people)
        l = 0
        r = n-1
        ret = 0
        
        while l <= r:
            val = people[l] + people[r]
            if val <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
                
            ret += 1
            
        return ret
        
