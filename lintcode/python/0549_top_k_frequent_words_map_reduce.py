
# there is an issue with the lintcode question

'''
Definition of Document
class Document:
    def __init__(self, id, content):
        self.id = id
        self.content = content
'''
from Mr_tools import Document
class TopKFrequentWords:
    # @param {Document} value is a document and value have two attributes(id and content)
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        # key is word and value is 1
        for word in value.content.split():
            yield word, 1

        return

    # @param key is from mapper
    # @param values is a list of document
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        # key is word, value is count
        yield key, values
        
        return
