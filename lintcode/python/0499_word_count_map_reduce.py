class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        words = line.split()
        for w in words:
            yield w, 1
            
        return


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        ret = 0
        
        for v in values:
            ret += v
            
        yield key, ret
        
        return
