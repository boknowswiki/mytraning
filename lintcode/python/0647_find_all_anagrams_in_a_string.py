#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        if len(p) > len(s):
            return []
        if p == s:
            return [0]
            
        p_hash = {}
        s_hash = {}
        
        ans = [] 
        for i in range(len(p)):
            p_hash[p[i]] = p_hash.get(p[i],0) + 1 
            s_hash[s[i]] = s_hash.get(s[i],0) + 1 
            
        if s_hash == p_hash:
            ans.append(0)    
           
        for window_start in range(1,len(s) - len(p) + 1):
            window_end = window_start + len(p) - 1 
            s_hash[s[window_end]] = s_hash.get(s[window_end], 0) + 1 
            
            s_hash[s[window_start -1]] -= 1 
            if s_hash[s[window_start -1]] == 0:
                del s_hash[s[window_start -1]]
            
            if s_hash == p_hash:
                ans.append(window_start)
                
        return ans
            
            
            
