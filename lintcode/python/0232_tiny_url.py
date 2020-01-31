#!/usr/bin/python -t

# hash table

class TinyUrl:
    def __init__(self):
        self.d = {}
        
    def idToShortKey(self, id):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        short_key = ""
        
        while id > 0:
            short_key = chars[id%62] + short_key
            id = id/62
            
        while len(short_key) < 6:
            short_key = 'a' + short_key
            
        return short_key
    
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        # write your code here
        id = 0
        
        for s in url:
            id = (id * 256 + ord(s)) % 56800235584L
            
        while id in self.d:
            id = (id + 1) % 56800235584L
            
        self.d[id] = url
        
        return "http://tiny.url/" + self.idToShortKey(id)
        
    def shortKeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        # write your code here
        return self.d[self.shortKeyToid(url[-6:])]
        

