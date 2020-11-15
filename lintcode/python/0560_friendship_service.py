#!/usr/bin/python -t

class FriendshipService:
    
    def __init__(self):
        # do intialization if necessary
        self.followers = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        # write your code here
        if user_id in self.followers:
            ret = list(self.followers[user_id])
            ret.sort()
            return ret
            
        return []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        # write your code here
        if user_id in self.followings:
            ret = list(self.followings[user_id])
            ret.sort()
            return ret
            
        return []

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        # write your code here
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
            
        self.followers[to_user_id].add(from_user_id)
        self.followings[from_user_id].add(to_user_id)
        return

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        # write your code here
        if to_user_id not in self.followers or from_user_id not in self.followings:
            return
        
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)
                
        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)
        
        return
