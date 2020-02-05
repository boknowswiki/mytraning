#!/usr/bin/python -t

# hash table
# 利用hashset判断是否已经出现过一次，若已经出现，记录答案。


# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            if substring in record:
                r.add(substring)
            else:
                record.add(substring)
        return list(r)


class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        d = {}
        n = len(s)
        
        for i in range(n-9):
            ss = s[i:i+10]
            #print ss
            d[ss] = d.get(ss, 0) + 1
            
        ret = []
        #print d
        
        for k in d:
            if d[k] > 1:
                ret.append(k)
                
        return ret
        
