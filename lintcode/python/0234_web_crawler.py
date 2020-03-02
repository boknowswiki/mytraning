#!/usr/bin/python -t

# bfs and dfs
# multithreading

"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""

import threading


class Solution:
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    def crawler(self, url):
        # write your code here
        self.v = set([url])
        self.threads = []
        
        self.dfs(url)
        
        for thread in self.threads:
            thread.join()
            
        return list(self.v)
        
    def dfs(self, url):
        sub_urls = HtmlHelper.parseUrls(url)
        for sub_url in sub_urls:
            if "wikipedia" not in sub_url:
                continue
            if sub_url in self.v:
                continue
            self.v.add(sub_url)
            if threading.activeCount() < 3:
                thread = threading.Thread(target=self.dfs, args=(sub_url, ))
                self.threads.append(thread)
                thread.start()
            else:
                self.dfs(sub_url)
                
        

"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""

import threading
import time
import collections
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def __init__(self):
        self.q = collections.deque()
        self.v = set()
        self.jobs = 0
        self.lock = threading.Lock()
        
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    def crawler(self, url):
        # write your code here
        self.q.append(url)
        pool_executor = ThreadPoolExecutor(max_workers=3)
        
        while self.q or self.jobs != 0:
            if not self.q:
                time.sleep(0.5)
                continue
        
            try:
                new_url = self.q.popleft()
                
                if new_url not in self.v:
                    self.v.add(new_url)
                    self.lock.acquire()
                    self.jobs += 1
                    self.lock.release()
                    
                    pool_executor.submit(self.get_new_urls, new_url)
                    
            except Exception as e:
                continue
            
        return list(self.v)
        
    def get_new_urls(self, url):
        sub_urls = HtmlHelper.parseUrls(url)
        
        for sub_url in sub_urls:
            if "wikipedia" not in sub_url:
                continue
            self.q.append(sub_url)
            
        self.lock.acquire()
        self.jobs -= 1
        self.lock.release()
        
        return
    



"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""

import threading

class Solution:
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    def crawler(self, url):
        self.queue = [url]
        self.urlSet = set([url])
        self.threads = []
        
        self.bfs()
        
        for thread in self.threads:
            thread.join()
        
        return list(self.urlSet)
    
    def bfs(self):
        while len(self.queue):
            url = self.queue.pop(0)
            sub_urls = HtmlHelper.parseUrls(url)
            for sub_url in sub_urls:
                if not "wikipedia" in sub_url:
                    continue
                if sub_url in self.urlSet:
                    continue
                self.urlSet.add(sub_url)
                self.queue.append(sub_url)
                if threading.activeCount() < 3:
                    thread = threading.Thread(target = self.bfs, args = (self, ))
                    self.threads.append(thread)
                    thread.start()
