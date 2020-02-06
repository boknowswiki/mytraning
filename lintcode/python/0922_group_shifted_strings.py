#!/usr/bin/python -t

# hash table

# 把每个字符串平移到第一个字母为A，就用这个字符串作为KEY。随后用HASHMAP进行归类

class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        # write your code here
        d = {}
        ret = []
        
        for s in strings:
            diff = ord(s[0]) - ord('a')
            tmp = ""
            for c in s:
                shift_diff = chr(ord(c) - diff)
                if shift_diff < 'a':
                    shift_diff = chr(ord(shift_diff)+26)
                    
                tmp += shift_diff
                
            if tmp not in d:
                d[tmp] = []
            
            d[tmp].append(s)
                
        for k in d:
            ret.append(d[k])
            
        return ret
        
