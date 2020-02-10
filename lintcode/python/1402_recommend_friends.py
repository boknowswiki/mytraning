#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """
    def recommendFriends(self, friends, user):
        # Write your code here
        n = len(friends)
        f_list = friends[user]
        max_com = 0
        ret = -1
        
        for i in range(n):
            if i != user and i not in f_list:
                other_list = friends[i]
                comm = 0
                for other_ele in other_list:
                    if other_ele in f_list:
                        comm += 1
                    if comm > max_com:
                        max_com = comm
                        ret = i
                        
        return ret
                        
                

class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """
    def recommendFriends(self, friends, user):
        # Write your code here 
        n = len(friends)
        userSet = {}
        ans = 0
        idx = -1
        for i in friends[user]:
            userSet[i] = i
        for i in range(n):
            if i == user or userSet.has_key(i):
                continue
            t = 0
            for j in friends[i]:
                if userSet.has_key(j):
                    t = t + 1
            if t > ans:
                ans = t
                idx = i
        return idx

