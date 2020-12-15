'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''


class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        rt = {}
        for doc in docs:
            for word in doc.content.split():
                if word in rt:
                    if rt[word][-1] != doc.id:
                        rt[word].append(doc.id)
                else:
                    rt[word] = [doc.id]
        return rt


class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        if not docs:
            return None
        
        ret = {}    
        
        for d in docs:
            words = d.content.split()
            v = set()
            for w in words:
                if w in v:
                    continue
                v.add(w)
                if w not in ret:
                    ret[w] = []
                ret[w].append(d.id)
                
        return ret
                
