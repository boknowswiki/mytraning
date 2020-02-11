#!/usr/bin/python -t

# hash table
# 本题不可出现的词汇位于set中，显然只需要对每个单词截取后，进行查询，存入HashMap计数即可。每次更新维护最大值和答案即可。

class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        w_list = s.split(",")
        words_list = []
        for ele in w_list:
            words_list.extend(ele.split(" "))
            
        #print words_list
        d = {}
        max_cnt = 0
        
        for word in words_list:
            if word not in excludewords and len(word) > 0:
                d[word] = d.get(word, 0) + 1
                max_cnt = max(max_cnt, d[word])
                
        ret = []
        for k in d:
            if d[k] == max_cnt:
                ret.append(k)
                
        ret.sort()
        return ret[0]
        

# 本题利用python实现单词的截取，考虑正则表达式re.findall(r"\b\S+\b", s)。
# tip:\b表示单词的开头或者结尾，\S表示非空白符任意字符，+表示前面字符可以重复一次以上，最后返回一个列表。

import re
class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        ans={}
        now=0
        s=" "+s
        lst = re.findall(r"\b\S+\b", s) 
        for x in lst:
            if x not in excludewords:
                if ans.__contains__(x) :
                    ans[x]+=1
                else :
                    ans[x]=1
                if ans[x]>now:
                    now=ans[x]
                    res=x
                elif ans[x]==now:
                    if x<res:
                        res=x
        return res
