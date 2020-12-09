class NGram:

    # @param {int} n a integer
    # @param {str} string a string
    def mapper(self, _, n, string):
        # Write your code here
        # Please use 'yield key, value' here
        for i in range(0, len(string)-n+1):
            s = string[i:i+n]
            #print s
            yield s, 1
                
        return


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, sum(values)
        
        return
