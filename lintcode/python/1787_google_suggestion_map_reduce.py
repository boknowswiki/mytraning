'''
Definition of Document
class Document:
    def __init__(self, word, count):
        self.word = word
        self.count = count
'''
from Mr_tools import Document
class GoogleSuggestion:
    # @param {Document} value is a document and value have two attributes(word and count)
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        # key is prefix and value is document
        #print value.word
        words = value.word
        key = ""
        for word in words:
            key += word # key = words[:i+1] for i in range(len(words))
            my_value = Document(words,value.count)
            yield key,my_value


    # @param key is from mapper
    # @param values is a list of document
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        # key is prefix, value is ordered list of document
        values = sorted(values,key=lambda x:(-x.count,x.word)) # sorted from largest to smallest 
        index = 0
        list_len = len(values)
        results = values[:10] if len(values) > 10 else values[:list_len] 
        yield key,results
        
