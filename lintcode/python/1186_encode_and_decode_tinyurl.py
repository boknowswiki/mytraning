#!/usr/bin/python -t

# hash table

class Solution:
    def __init__(self):
        self.l2s = {}
        self.s2l = {}
        self.base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.global_id = -1

    def get_next_id(self):
        self.global_id +=1
        return self.global_id

    def encode_base62(self, global_id):
        ret = ""

        while global_id > 0:
            ret = self.base62[global_id%62] + ret
            global_id = global_id // 62
        
        while len(ret) < 6:
            ret = "0" + ret

        return ret

    def encode(self, longUrl):
        # Encodes a URL to a shortened URL.
        if longUrl in self.l2s:
            return self.l2s[longUrl]
        
        global_id = self.get_next_id()
        short_url = self.encode_base62(global_id)
        self.l2s[longUrl] = short_url
        self.s2l[short_url] = longUrl

        return short_url

    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        return self.s2l[shortUrl]

# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));



import random

class Solution:
    def __init__(self):
        self.dic = {}
        self.dic2 = {}
    def encode(self, longUrl):
        # Encodes a URL to a shortened URL.
        self.dic[longUrl] = str(random.randint(1,100))
        self.dic2["https://tinyurl.com/" + self.dic[longUrl]] = longUrl
        return "https://tinyurl.com/" + self.dic[longUrl]

    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        return self.dic2[shortUrl]

# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));
