#!usr/bin/python -t

'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        # do intialization if necessary
        BaseGFSClient.__init__(self)
        self.cs = chunkSize
        self.d = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code here
        if filename not in self.d:
            return None
            
        ret = ""
        
        for i in range(len(self.d[filename])):
            has = self.readChunk(filename, self.d[filename][i])
            if has:
                ret += has
            
        return ret

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        n = len(content)
        self.d[filename] = []
        index = 0
        cs = n/self.cs
        if n%self.cs:
            cs +=1

        for i in range(cs):
            self.d[filename].append(i)
            subcontent = content[self.cs*i: (i+1)*self.cs]
            self.writeChunk(filename, i, subcontent)

        return                

