#!/usr/bin/python -t

# hash table
#欲记录单词出现的次数, 首选是哈希表. 大多高级语言内置相关的数据结构, 编码简单.
#
#使用哈希表记录每个单词出现的次数, 然后需要将单词按照 次数(主要关键词)和字典序(次要关键字) 排序, 取出前k个即可.
#
#排序的过程可以用 heap, 也可以使用快排等排序算法.

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        n = len(words)
        d = {}
        
        for w in words:
            d[w] = d.get(w, 0) + 1
            
        l = []
        for key, value in d.items():
            l.append((value, key))
            
        l.sort(cmp = self.cmp)
        
        ret = []
        
        for i in range(k):
            ret.append(l[i][1])
            
        return ret
        
    def cmp(self, a, b):
        if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
            return -1
        elif a[0] == b[0] and a[1] == b[1]:
            return 0
        else:
            return 1
            
            
            
