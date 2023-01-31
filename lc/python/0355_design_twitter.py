# design, hash map, sort

class Twitter:

    def __init__(self):
        self.cap = 10
        self.db = collections.defaultdict(list)
        self.fol = collections.defaultdict(list)
        self.index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.db[userId].append((self.index, tweetId))
        self.index += 1
        if len(self.db[userId]) > self.cap:
            self.db[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        ret_list = []
        #print(f"user id {userId} db {self.db[userId]}")
        ret_list.extend(self.db[userId])
        #print(f"ret list {ret_list}")
        for follow in self.fol[userId]:
            ret_list.extend(self.db[follow])

        #print(f"ret list {ret_list}")
        ret_int_list = sorted(ret_list, key=lambda x: -x[0])[:10]
        return [x[1] for x in ret_int_list]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.fol[followerId]:
            self.fol[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fol[followerId]:
            self.fol[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


# other people's answer:

class Twitter:
    
    def __init__(self):
        self.followers_dict = defaultdict(set)
        self.tweets_dict = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        import time
        time.sleep(0.01)
        self.tweets_dict[userId].add( (time.time(), tweetId) )

    def getNewsFeed(self, userId: int) -> List[int]:
        import time
        list_of_users = set(self.followers_dict[userId])
        list_of_users.add(userId)
        posts_heap = []
        
        for user in list_of_users:
            for post in self.tweets_dict[user]:
                diff = time.time() - post[0]
                heapq.heappush(posts_heap, [diff, post[1]])

        count = 0
        tweet_ids = []
        while posts_heap and count < 10:
            temp_post = heapq.heappop(posts_heap)
            tweet_ids.append(temp_post[1])
            count += 1
        
        return tweet_ids


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_dict[followerId]:
            self.followers_dict[followerId].remove(followeeId)


import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followee = {}
        

    def postTweet(self, user, tweet):
        self.time += 1
        self.tweets[user] = self.tweets.get(user, []) + [(-self.time,  tweet)]
        
        

    def getNewsFeed(self, user):
        h, tweets = [], self.tweets
        people = self.followee.get(user, set()) | set([user])
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:
                    new_time, new_tweet = tweets[person][idx-1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news
        
        

    def follow(self, follower, other):
        self.followee[follower] = self.followee.get(follower, set()) | set([other])
        
        

    def unfollow(self, follower, other):
        if follower in self.followee:
            self.followee[follower].discard(other)
