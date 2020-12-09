'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        words = value.content.split()
        for w in words:
            yield w, value.id

        return

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, sorted(list(set(values)))
            
        return


'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        words = value.content.split()
        for w in words:
            yield w, value.id

        return

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        ret = []
        for v in values:
            if v not in ret:
                ret.append(v)
            
        yield key, sorted(ret)
        
        return
