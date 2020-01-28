#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        str_list = teststr.split()
        
        d = {}
        s = set()
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if str_list[i] not in s:
                    d[pattern[i]] = str_list[i]
                    s.add(str_list[i])
                else:
                    return False
            else:
                if d[pattern[i]] != str_list[i]:
                    return False
                    
        return True
        
