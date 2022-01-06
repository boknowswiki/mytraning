#!/usr/bin/python -t

# heap


import heapq

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        d = {}
        for result in results:
            if result.id not in d:
                d[result.id] = []

            heapq.heappush(d[result.id], result.score)
            if len(d[result.id]) > 5:
                heapq.heappop(d[result.id])
        #print(d)
        ret = {}
        for k in d:
            ret[k] = (sum(d[k])/5)

        return ret

# heap
# 利用map，找到对应的人的成绩，然后暴力比较出前5个。

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

import heapq

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        n = len(results)
        d = {}
        ret = {}
        
        for i in range(n):
            id, score = results[i].id, results[i].score
            if id not in d:
                d[id] = [score]
            else:
                d[id].append(score)
                
        #print d
                
        for k in d:
            scores = d[k]
            #print scores
            heap = []
            for s in scores:
                heapq.heappush(heap, s)
                if len(heap) > 5:
                    heapq.heappop(heap)
                    
            #print heap
            avg = self.getAvg(heap)
            ret[k] = avg
            
        return ret
        
    def getAvg(self, l):
        #print l
        avg = 0
        for ll in l:
            avg += ll
            
        return float(avg)/len(l)
        
