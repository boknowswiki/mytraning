#!/usr/bin/python -t

# hash table
# 利用dict 来维护相似字符串之间的关系（因为一个字符串可能会映射多个串，所以使用String和dict的映射关系）,在判断两个字符串是否相似时，只需要直接判断两字符串是否相等，如果不相等的话，就查询dict来判断字符串是否相似即可

class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        m = len(words1)
        n = len(words2)
        if m != n:
            return False
            
        d = {}
        
        for i in range(len(pairs)):
            s = set()
            if d.get(pairs[i][0]) != None:
                s = d[pairs[i][0]]
            s.add(pairs[i][1])
            d[pairs[i][0]] = s
            
        #print d
        
        for i in range(m):
            if words2[i] == words1[i]:
                continue
            
            if (d.get(words1[i]) == None or words2[i] not in d[words1[i]]) and (d.get(words2[i]) == None or words1[i] not in d[words2[i]]):
                return False
                
        return True
        
        
