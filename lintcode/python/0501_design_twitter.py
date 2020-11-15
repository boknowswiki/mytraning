#!/usr/bin/python -t

# 因为题目里涉及到对推文按照时间排序, 同时 Tweet 类本身不含时间信息, 所以我们需要额外地记录每条推文发出的时间.
# 
# 可以定义一个类的静态变量作为计数器来实现.
# 
# 然后分析我们需要的数据结构:
# 
# class Node {Tweet, int}; 对原有的Tweet类的扩展, 使其可以记录时间 (当然, 也可以用类的继承来实现)
# map<int, vector<Node>> 用户id到这个用户发送了的推文的映射
# map<int, set<int>> 用户id到这个用户关注的人的id的映射
# 然后对应每种方法的实现:
# 
# postTweet() 直接添加到map<int, vector<Node>>中即可
# getTimeline() 根据map<int, vector<Node>>获得该用户的最新推文, 返回即可
# getNewsFeed() 同时用到上面定义的两个映射, 比较暴力的做法是获取这些用户的所有推文, 排序, 拿出前十个; 或者可以利用堆进行 "多路归并"
# follow() 在 map<int, set<int>> 中添加即可
# unfollow() 在 map<int, set<int>> 中删除即可

'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.friends = {}
        self.user = {}
        self.order = 0

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        tweet = Tweet.create(user_id, tweet_text)
        self.order += 1
        
        if user_id not in self.user:
            self.user[user_id] = []
            
        self.user[user_id].append((self.order, tweet))
        
        return tweet
        
        

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        tweets = []
        if user_id in self.user:
            tweets = self.user[user_id][-10:]
            
        if user_id in self.friends:
            for f in self.friends[user_id]:
                if f in self.user:
                    tweets.extend(self.user[f][-10:])
            
        tweets.sort(cmp=lambda x, y: cmp(x[0], y[0]))
        
        return [tweet[1] for tweet in tweets[-10:][::-1]]
        

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if user_id in self.user:
            return [tweet[1] for tweet in self.user[user_id][-10:][::-1]]
            
        return []
        

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.friends:
            self.friends[from_user_id] = set()
            
        self.friends[from_user_id].add(to_user_id)
        return

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id in self.friends:
            self.friends[from_user_id].remove(to_user_id)
        return
