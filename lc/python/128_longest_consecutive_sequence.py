#!/usr/bin/python -t

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# hash map
# time O(n)
# space O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set()
        v = set()

        for num in nums:
            num_set.add(num)

        start = end = 0
        ret = 0

        for num in num_set:
            if num not in v:
                v.add(num)
                start = end = num
                while start in num_set:
                    v.add(start)
                    start -= 1
                while end in num_set:
                    v.add(end)
                    end += 1
                ret = max(ret, end-start-1)

        return ret

class uf(object):
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
        self.size = [1]*n
        #print self.father
        
    def find(self, p):
        #print p, self.father
        while p != self.father[p]:
            self.father[p] = self.father[self.father[p]]
            p = self.father[p]
        
        #print "return %d" % p
        return p
        
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        
        #self.father[proot] = self.father[qroot]
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = qroot
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = proot
            self.size[proot] = self.size[proot] + self.size[qroot]

        #print proot, qroot, self.father
        
        
    def maxCount(self):
        mymax = 0
        for size in self.size:
            mymax = max(mymax, size)
            
        return mymax

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        
        n = len(nums)
        
        myuf = uf(n)
        
        for i in range(n):
            if nums[i] in d:
                continue
                
            d[nums[i]] = i
            
            if nums[i]+1 in d:
                myuf.union(i, d[nums[i]+1])
            if nums[i]-1 in d:
                myuf.union(i, d[nums[i]-1])
                
        return myuf.maxCount()

if __name__ =='__main__':
    s = [100,4,200,1,3,2]
    ss = Solution()
    print('answer is %d' % ss.longestConsecutive(s))
