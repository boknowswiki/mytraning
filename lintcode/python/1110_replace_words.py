#!/usr/bin/python -t

# hash table

# 字典树，O（n）完成字符前缀匹配

class Solution:
    """
    @param dict: List[str]
    @param sentence: a string
    @return: return a string
    """
    def replaceWords(self, dict, sentence):
        # write your code here
        words = sentence.split(" ")
        for i in range(len(words)):
            for root in dict:
                if root in words[i]:
                    len_match = len(root)
                    if len_match < words[i] and words[i][:len_match] == root:
                        words[i] = root
                        
        return " ".join(words)
        
        
