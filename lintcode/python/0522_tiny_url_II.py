#!/usr/bin/python -t

# hash table


class TinyUrl2:
    def __init__(self):
        self.l2s = {}
        self.s2l = {}
        self.cnt = 0
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.short_prev = "http://tiny.url/"
        
    def getNewShort(self, url):
        ret = ""
        tmp = self.cnt
        
        for i in range(6):
            ret += self.chars[tmp%62]
            tmp //= 62
            
        self.cnt += 1
        return self.short_prev + ret
        
    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        # write your code here
        custom_url = self.short_prev+key
        if long_url in self.l2s:
            if self.l2s[long_url] != custom_url:
                return "error"
            else:
                return custom_url
        if custom_url in self.s2l:
            return "error"
            
        self.l2s[long_url] = custom_url
        self.s2l[custom_url] = long_url
    
        return custom_url

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        # write your code here
        if long_url in self.l2s:
            return self.l2s[long_url]
            
        short_url = self.getNewShort(long_url)
        self.l2s[long_url] = short_url
        self.s2l[short_url] = long_url
        return short_url
        
    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        # write your code here
        if short_url in self.s2l:
            return self.s2l[short_url]
        else:
            return "error"
            


class TinyUrl2:

    # @param long_url a long url
    # @param a short key
    # @return a short url starts with http://tiny.url/
    def __init__(self):
        self.globalId = 0
        self.id2url = {}
        self.url2id = {}
        self.customLong2Short = {}
        self.customShort2Long = {}
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    def createCustom(self, long_url, short_key):
        # Write your code here
        if long_url in self.customLong2Short:
            if short_key == self.customLong2Short[long_url]:
                return "http://tiny.url/"+short_key
            return "error"
        if short_key in self.customShort2Long:
            if long_url == self.customShort2Long[short_key]:
                return "http://tiny.url/"+short_key
            return "error"
        self.customLong2Short[long_url] = short_key
        self.customShort2Long[short_key] = long_url
        return "http://tiny.url/"+short_key

    
    # @param {string} long_url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, long_url):
        # Write your code here
        if long_url in self.customLong2Short:
            return "http://tiny.url/" + self.customLong2Short[long_url]
        if long_url in self.url2id:
            return "http://tiny.url/" + self.id2Short(self.url2id[long_url])
        self.globalId += 1
        self.id2url[self.globalId] = long_url
        self.url2id[long_url] = self.globalId
        return "http://tiny.url/" + self.id2Short(self.globalId)

    def id2Short(self, id):
        s = ""
        while id > 0:
            s = self.chars[id%62]+s
            id /= 62
        while len(s) < 6:
            s = 'a'+s
        return s

    # @param {string} short_url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, short_url):
        # Write your code here
        short_key = self.getShort(short_url)
        if short_key in self.customShort2Long:
            return self.customShort2Long[short_key]
        id = self.short2Id(short_key)
        return self.id2url.get(id)
    
    def getShort(self, short_url):
        return short_url[len("http://tiny.url/"):]
        
    def short2Id(self, short):
        id = 0
        for ch in short:
            id = id*62 + self.chars.index(ch)
        return id


