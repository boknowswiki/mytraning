#!/usr/bin/python -t

# hash table


class Solution:
    """
    @param names: a string array
    @return: the string array
    """
    def DistinguishUsername(self, names):
        # Write your code here
        n = len(names)
        d = {}
        ret = []
        
        for i in range(n):
            if names[i] in d:
                cnt = d[names[i]]
                d[names[i]] += 1
            else:
                d[names[i]] = 1
                cnt = 0
                
            if cnt != 0:
                ret.append(names[i]+str(cnt))
            else:
                ret.append(names[i])
        return ret
        
        

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param names: a string array
    @return: the string array
    """
    def DistinguishUsername(self, names):
        # Write your code here
        hashMap = {}        #字典计数
        results = []
        for name in names:
            if name in hashMap:
                count = hashMap[name]
                hashMap[name] += 1
                results.append(name + str(count))   #将数字转为字符串加到原字符串后面
            else:
                hashMap[name] = 1
                results.append(name)    #第一次出现原样存入答案
        return results
